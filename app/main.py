from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi import Form

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.database import (
    SessionLocal,
    engine
)

from app import models

from app.schemas import URLRequest

from app.crud import (
    create_short_url,
    get_url_by_code,
    increment_clicks
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener Service")

BASE_URL = "http://127.0.0.1:8000"

# Static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# Templates
templates = Jinja2Templates(directory="app/templates")


# Database dependency

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "short_url": None
        }
    )


# Form submit endpoint
@app.post("/shorten", response_class=HTMLResponse)
def shorten_url(
    request: Request,
    original_url: str = Form(...),
    db: Session = Depends(get_db)
):

    db_url = create_short_url(
        db,
        original_url
    )

    short_url = f"{BASE_URL}/{db_url.short_code}"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "short_url": short_url
        }
    )



# Redirect endpoint
@app.get("/{short_code}")
def redirect_to_url(
    short_code: str,
    db: Session = Depends(get_db)
):

    db_url = get_url_by_code(
        db,
        short_code
    )

    if not db_url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    increment_clicks(db, db_url)

    return RedirectResponse(
        url=db_url.original_url
    )


# Stats endpoint
@app.get("/stats/{short_code}")
def get_stats(
    short_code: str,
    db: Session = Depends(get_db)
):

    db_url = get_url_by_code(
        db,
        short_code
    )

    if not db_url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return {
        "original_url": db_url.original_url,
        "short_code": db_url.short_code,
        "clicks": db_url.clicks,
        "created_at": db_url.created_at
    }