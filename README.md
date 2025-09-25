# Tallyradix
# Simple Journal Entry API (Django + DRF)

A lightweight and modular accounting journal entry API built with **Django** and **Django REST Framework (DRF)**.  
This project aims to provide a simple yet extensible way to handle double-entry bookkeeping as an API, so it can be integrated into B2C marketplaces, e-commerce platforms, or other systems that require automated accounting.

---

## Features

- 🔹 RESTful API for journal entries (create, list, query)
- 🔹 Double-entry bookkeeping support (debit/credit balance check)
- 🔹 Encryption support for sensitive data (AES256 with Fernet)
- 🔹 Containerized (Docker-ready)
- 🔹 Extensible for integration into SaaS or other platforms

---

## Tech Stack

- **Backend**: Django 5.x, Django REST Framework
- **Database**: PostgreSQL (recommended, but SQLite supported for development)
- **Security**: AES encryption (Fernet)
- **Containerization**: Docker + Docker Compose

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/devseventeen-jp/journal-entry-api.git
cd journal-entry-api
```
---

### 2. Environment Setup

Generate a Fernet key:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Create .env and adjust:

```env
DJANGO_SECRET_KEY=supersecretkey
DEBUG=1
DATABASE_URL=postgres://postgres:postgres@db:5432/accounting_db
DJANGO_LANGUAGE_CODE=ja
DJANGO_TIME_ZONE=Asia/Tokyo
AES_KEY=your-fernet-key
TOKEN_EXPIRE_DAYS=30
```
---

### 3. Install Dependencies

```bash
pip install -r requirements.dev.txt

```
------

### 4. Run with Docker

```bash
docker-compose up --build
```

The API will be available at:
👉 http://localhost:8000/api/journal/

---
## API Quickstart

This section demonstrates how to interact with the Journal API using `curl`.

### Obtain a Token

First, obtain an authentication token using your admin credentials:

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "your_admin_password"}'
```

The response will contain a token:

```json
{"token": "123abc456def..."}
```

Use this token in subsequent requests.

### Create a Journal Entry

```bash
curl -X POST http://localhost:8000/api/journal-entries/ \
  -H "Authorization: Token 123abc456def..." \
  -H "Content-Type: application/json" \
  -d '{
        "transaction_id": "550e8400-e29b-41d4-a716-446655440000",
        "description": "Digital product sale",
        "entries": [
          {
            "account_code": "4000",
            "account_name": "Revenue",
            "debit": 0,
            "credit": 1000
          },
          {
            "account_code": "1110",
            "account_name": "Cash",
            "debit": 1000,
            "credit": 0
          }
        ]
      }'
```

### Retrieve Journal Entries

```bash
curl -X GET http://localhost:8000/api/journal-entries/ \
  -H "Authorization: Token 123abc456def..."
```

## Notes

- 🔹 Make sure your Django server is running on http://localhost:8000
- 🔹 An admin user must be created beforehand (python manage.py createsuperuser)
- 🔹 The transaction_id must be a valid UUID. You can generate one with:
    - 🔹 CLinux / macOS: uuidgen
    - 🔹 Windows PowerShell: [guid]::NewGuid()

## Security Considerations

- 🔹 .env files must not be committed to version control.
- 🔹 The provided token authentication is intended for development and testing.
    　For production, consider replacing it with JWT or OAuth2.
- 🔹 Always use HTTPS in production deployments.
