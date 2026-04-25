from fastapi import FastAPI, HTTPException, RedirectResponse
from pydantic import BaseModel
import string
import random

app = FastAPI(title="URL Shortener")

# In-memory storage for now (replace with SQLite later)
url_store = {}
base62 = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

def generate_short_code(length=6):
    return ''.join(random.choices(base62, k=length))

class URLRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "URL Shortener Service", "docs": "/docs"}

@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_code = generate_short_code()
    # Handle collision (simple retry)
    while short_code in url_store:
        short_code = generate_short_code()
    
    url_store[short_code] = request.url
    return {
        "short_code": short_code,
        "short_url": f"http://localhost:8000/{short_code}",
        "original_url": request.url
    }

@app.get("/{short_code}")
def redirect_url(short_code: str):
    if short_code not in url_store:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=url_store[short_code])