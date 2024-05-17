FROM python:3.9-slim

# Configuración de la aplicación
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]