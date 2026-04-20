# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copy requirements first (layer caching)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source + trained model
COPY app/ .

EXPOSE 5000

# Use gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
