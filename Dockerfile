FROM python:3.11-slim

# Working folder
WORKDIR /app

# Copy files
COPY requirements.txt .

# Install library
RUN pip install --no-cache-dir -r requirements.txt

# Copy projetc
COPY . .

# Open ports
EXPOSE 8000

# Boot server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
