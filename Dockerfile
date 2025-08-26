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

# Enable execute entrypoint script
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
