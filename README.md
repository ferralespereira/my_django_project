# My Django Project - Auto Dealer CRUD

A Django web application for managing dealer vehicle inventory (Autos) with full CRUD operations and a Bootstrap UI.

## Features

- Auto inventory management (Create, Read, Update, Delete)
- Django Admin integration for managing data
- Bootstrap 5 styling via CDN
- SQLite database for local development

## Tech Stack

- Python 3
- Django 6.0.3
- SQLite3
- Bootstrap 5.3 (CDN)

## Project Structure

```text
my_django_project/
├── manage.py
├── myproject/          # Project settings and root URLs
├── myapp/              # App with models, views, urls, admin
├── templates/          # Global templates
├── db.sqlite3          # SQLite database
└── README.md
```

## Auto Model Fields

The `Auto` model includes:

- `brand`
- `model`
- `year`
- `price`
- `color`
- `transmission` (`manual`, `automatic`)
- `fuel_type` (`gasoline`, `diesel`, `electric`, `hybrid`)
- `mileage`
- `description`
- `created_at`, `updated_at`

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/ferralespereira/my_django_project.git
cd my_django_project
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install django
```

4. Run migrations:

```bash
python manage.py migrate
```

5. (Optional) Create an admin user:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open in browser:

- App home: `http://127.0.0.1:8000/`
- Auto list: `http://127.0.0.1:8000/autos/`
- Admin: `http://127.0.0.1:8000/admin/`

## CRUD Routes

- `GET /autos/` - list autos
- `GET /autos/create/` - auto create form
- `POST /autos/create/` - create auto
- `GET /autos/<id>/` - auto detail
- `GET /autos/<id>/edit/` - auto edit form
- `POST /autos/<id>/edit/` - update auto
- `GET /autos/<id>/delete/` - delete confirmation
- `POST /autos/<id>/delete/` - delete auto

## Notes

- This project uses SQLite (`db.sqlite3`) by default.
- Development settings are enabled (`DEBUG = True`).
- For production, configure environment variables, allowed hosts, static files, and a production database.
