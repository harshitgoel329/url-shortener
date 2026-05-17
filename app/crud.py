from sqlalchemy.orm import Session

from app.models import URL
from app.utils import generate_short_code


# Create short URL

def create_short_url(db: Session, original_url: str):

    short_code = generate_short_code()

    # Collision handling
    while db.query(URL).filter(
        URL.short_code == short_code
    ).first():

        short_code = generate_short_code()

    db_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url


# Get URL by short code

def get_url_by_code(db: Session, short_code: str):

    return db.query(URL).filter(
        URL.short_code == short_code
    ).first()


# Increment click count

def increment_clicks(db: Session, url):

    url.clicks += 1

    db.commit()

    db.refresh(url)

    return url