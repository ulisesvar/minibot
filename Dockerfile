# Imagen base de Python (ligera y moderna)
FROM python:3.11-slim

# Evita archivos .pyc y mejora los logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código al contenedor
COPY . .

# Comando para ejecutar el script principal
CMD ["python", "minibot.py"]
