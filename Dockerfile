# 1. Usar una imagen base de Python ligera
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto de tu código (main.py)
COPY . .

# 5. Exponer el puerto par que podamos conectarnos
EXPOSE 8000

# 6. Comando para arrancar el servidor web
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]