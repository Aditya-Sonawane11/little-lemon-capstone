# Little Lemon Restaurant API

A Django + Django REST Framework capstone project. It serves a static restaurant landing page, exposes menu and table-booking APIs, supports registration/token authentication, and uses **MySQL** as its configured database.

## Features

- Django serves the static HTML landing page at `/`.
- Menu CRUD API: `/api/menu/items/` (read-only to anonymous visitors; authenticated users can write).
- Table booking CRUD API: `/api/booking/tables/` (authentication required; customers see and manage their own bookings; staff can view all).
- User registration: `POST /api/registration/`.
- Token login: `POST /api/token/login/`.
- Django admin for menu items and bookings: `/admin/`.
- Automated API tests.
- MySQL 8 Docker Compose configuration.
- Insomnia import collection in `insomnia/`.

## Quick start (recommended: MySQL with Docker)

Requirements: Python 3.10+, Docker Desktop, and a working C/C++ build environment if your platform needs to compile `mysqlclient`.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .venv\Scripts\Activate.ps1
   # macOS/Linux:
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start MySQL:

   ```bash
   docker compose up -d db
   ```

   The development database is `littlelemon`, username `littlelemon`, password `littlelemon`, host `127.0.0.1`, port `3306`. Change these values for a real deployment.

4. Copy `.env.example` to `.env` and set your values. Django does not automatically load `.env`; either export the variables in your terminal or use your preferred environment loader. The defaults in `settings.py` match the local Docker Compose database.

5. Create tables and an admin account:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/`.

### Windows note for mysqlclient

If `pip install mysqlclient` fails on Windows, install the matching MySQL client development libraries / Visual C++ build tools, or use a Python environment where a compatible wheel is available. For a quick smoke test without MySQL, set `USE_SQLITE=True` before running migrations. The assessed configuration defaults to MySQL.

## API reference

All endpoints end with a trailing slash.

| Method | Endpoint | Purpose | Access |
|---|---|---|---|
| GET | `/api/menu/items/` | List menu items | Public |
| POST | `/api/menu/items/` | Create menu item | Authenticated |
| GET | `/api/menu/items/{id}/` | Retrieve menu item | Public |
| PUT/PATCH/DELETE | `/api/menu/items/{id}/` | Update/delete menu item | Authenticated |
| GET | `/api/booking/tables/` | List current user's bookings | Authenticated |
| POST | `/api/booking/tables/` | Create booking | Authenticated |
| GET | `/api/booking/tables/{id}/` | Retrieve own booking | Authenticated |
| PUT/PATCH/DELETE | `/api/booking/tables/{id}/` | Update/delete own booking | Authenticated |
| POST | `/api/registration/` | Register a user | Public |
| POST | `/api/token/login/` | Obtain an auth token | Public |

### Example requests

Register:

```json
{
  "username": "lemon_guest",
  "email": "guest@example.com",
  "password": "StrongPass123!"
}
```

Log in:

```json
{
  "username": "lemon_guest",
  "password": "StrongPass123!"
}
```

Use the returned token on protected endpoints:

```http
Authorization: Token YOUR_TOKEN_HERE
```

Create a booking:

```json
{
  "name": "Alex",
  "no_of_guests": 2,
  "booking_date": "2026-11-15T19:00:00+05:30"
}
```

Create a menu item:

```json
{
  "title": "Lemon dessert",
  "price": "8.50",
  "inventory": 15,
  "description": "A bright citrus dessert.",
  "category": "Dessert"
}
```

## Add sample menu data

Open `/admin/` and add menu items, or use the API while authenticated. The project intentionally starts with an empty menu rather than fabricated restaurant inventory.

## Run tests

```bash
python manage.py test
```

The tests cover public menu reads, menu write permissions, registration, booking creation, and booking validation.

## Insomnia

Import `insomnia/little-lemon-insomnia.json` into Insomnia. Set the `base_url` environment variable to `http://127.0.0.1:8000` and replace `YOUR_TOKEN_HERE` for authenticated requests.

## GitHub submission

Before submitting:

```bash
git init
git add .
git commit -m "Build Little Lemon Django REST API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/little-lemon-capstone.git
git push -u origin main
```

Paste the repository URL into the peer-review submission. Do not commit secrets, virtual environments, or your local database.

## Project structure

```text
little-lemon-capstone/
├── littlelemon/          # Django project configuration
├── restaurant/           # Models, serializers, API views, tests
├── templates/            # Static HTML page served by Django
├── static/               # CSS
├── insomnia/             # REST client request collection
├── docker-compose.yml    # MySQL service
├── manage.py
└── requirements.txt
```
