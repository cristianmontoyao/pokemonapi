# Dockerfile
FROM python:3.9-slim

# Configuración de la aplicación
WORKDIR /app
COPY . /app
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
