# Tallyradix
# Simple Journal Entry API (Django + DRF)

A lightweight and modular accounting journal entry API built with **Django** and **Django REST Framework (DRF)**.  
This project aims to provide a simple yet extensible way to handle double-entry bookkeeping as an API, so it can be integrated into C2C marketplaces, e-commerce platforms, or other systems that require automated accounting.

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

Create .env and adjust:

```env
DJANGO_SECRET_KEY=supersecretkey
DEBUG=1
DATABASE_URL=postgres://postgres:postgres@db:5432/accounting_db
DJANGO_LANGUAGE_CODE=ja
DJANGO_TIME_ZONE=Asia/Tokyo
AES_KEY=your-32-byte-key
TOKEN_EXPIRE_DAYS=30
```

Generate a Fernet key:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```
---

### 3. Run with Docker

```bash
docker-compose up --build
```

The API will be available at:
👉 http://localhost:8000/api/journal/

---