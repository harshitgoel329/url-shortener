# URL Shortener Service

A simple URL shortening service built with FastAPI.

## Tech Stack
- Python
- FastAPI
- SQLite (upcoming)
- Base62 encoding

## Features
- Generate short links from long URLs
- Redirect short URLs to original destinations
- Collision handling for short codes

## Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload