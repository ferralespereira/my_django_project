# EC2 Deployment Guide

## Prerequisites

- Ubuntu EC2 instance running
- SSH access
- `git` installed

## Steps

### 1. SSH into your EC2

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

### 2. Install dependencies

```bash
sudo apt update
sudo apt install python3-pip python3-venv git -y
```

### 3. Clone the repository

```bash
cd /var/www
sudo git clone https://github.com/ferralespereira/my_django_project.git
cd my_django_project
```

### 4. Create virtual environment and install packages

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Create .env file

```bash
cp .env.example .env
nano .env
```

Update with your:
- EC2 IP or domain in `ALLOWED_HOSTS`
- New `SECRET_KEY` (generate one: `python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- Set `DEBUG=False`

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 8. Collect static files

```bash
python manage.py collectstatic --noinput
```

### 9. Test the development server

```bash
python manage.py runserver 0.0.0.0:8000
```

Visit: `http://your-ec2-ip:8000`

### 10. Stop dev server (Ctrl+C) and proceed with production setup

For production, set up:
- Nginx (web server)
- Gunicorn (application server)
- PostgreSQL (database)
- SSL/TLS (Let's Encrypt)
- Systemd service (auto-restart)

Check `DEPLOYMENT.md` for full setup.
