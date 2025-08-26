#!/bin/sh
set -e

# Django migration
python manage.py migrate

# Ccreate admin user, when admin not exists
python - <<END
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.getenv("ADMIN_USER", "admin")
email = os.getenv("ADMIN_EMAIL", "admin@example.com")
password = os.getenv("ADMIN_PASS", "changeme!")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Admin user '{username}' created.")
else:
    print(f"Admin user '{username}' already exists.")
END

# Boot server
gunicorn project_root.wsgi:application --bind 0.0.0.0:8000
