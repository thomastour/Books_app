#  Books API (Django REST Framework)

This is a simple API for managing books and reviews, built with **Django REST Framework** and **Token Authentication** via `dj-rest-auth`.

---

## Technologies Used

- Python 
- Django
- Django REST Framework
- dj-rest-auth (login, registration)
- allauth
- SQLite3 (default DB)
- Token Authentication

---

## Features

- User registration and login
- Protected endpoints (with token)
- View all books
- Create, edit, and delete reviews
- Each user can see all reviews but can only modify their own

---

## ▶Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/thomastour/Books_app.git
cd Books_app
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate   # macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Start the development server**
```bash
python manage.py runserver
```

---

## 🔐 API Authentication

Uses `dj-rest-auth` with token authentication.

- POST `/api/auth/login/` → login and receive token
- POST `/api/auth/registration/` → create a new user

---

## API Endpoints

| Endpoint            | Method | Description                         |
|---------------------|--------|-------------------------------------|
| `/books/`           | GET    | Returns all books                   |
| `/reviews/`         | GET    | All reviews                         |
| `/reviews/`         | POST   | Create a review (only if logged in) |
| `/api/auth/login/`  | POST   | Login                               |
| `/api/auth/registration/` | POST | Register a new user          |

---
