# Dockerfile
FROM python:3.9-slim

# Configuración de la aplicación
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

CMD ["python", ".\main.py"]
