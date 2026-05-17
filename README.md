````md
# URL Shortener Service

A simple and efficient URL shortening service built using FastAPI and SQLite.  
This application converts long URLs into short, shareable links and redirects users to the original destination.

---

# Features

- Convert long URLs into short links
- Redirect short URLs to original destinations
- Persistent storage using SQLite
- Base62 short code generation
- Collision handling for unique short URLs
- Click tracking and analytics
- Simple and clean HTML/CSS frontend
- RESTful API using FastAPI
- Automatic API documentation with Swagger UI

---

# Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Jinja2 Templates
- HTML/CSS

---

# Project Structure

```text
url-shortener/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── utils.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── urls.db
````

---

# How It Works

1. User enters a long URL
2. Application generates a unique Base62 short code
3. URL mapping is stored in SQLite database
4. User receives a short URL
5. Accessing the short URL redirects to the original URL
6. Click count is tracked for analytics

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/harshitgoel329/url-shortener.git
```

## 2. Move Into Project Directory

```bash
cd url-shortener
```

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

---

# Open In Browser

Frontend:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Home Page

```http
GET /
```

Displays frontend UI.

---

## Shorten URL

```http
POST /shorten
```

### Form Data

| Field        | Type   | Description         |
| ------------ | ------ | ------------------- |
| original_url | string | Long URL to shorten |

---

## Redirect Endpoint

```http
GET /{short_code}
```

Redirects user to original URL.

---

## URL Statistics

```http
GET /stats/{short_code}
```

Returns:

* Original URL
* Short code
* Click count
* Creation timestamp

---

# Example

## Input URL

```text
https://www.google.com/search?q=fastapi
```

## Generated Short URL

```text
http://127.0.0.1:8000/aB12xY
```

---

# Future Improvements

* User authentication
* Custom aliases
* URL expiration
* QR code generation
* Redis caching
* Docker deployment
* PostgreSQL integration
* Rate limiting

---

# Learning Outcomes

This project helped in understanding:

* REST API development
* FastAPI framework
* Database integration using SQLAlchemy
* URL redirection
* Backend architecture
* CRUD operations
* Template rendering using Jinja2

---

# Author

Harshit Goel

GitHub:
[harshitgoel329/url-shortener]

```
```
