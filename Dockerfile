# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY DataReceiverAPI.py .
COPY InfoCollector.py .
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crea un directorio para los datos
RUN mkdir -p /app/data

# Exponer el puerto que utiliza la API
EXPOSE 5000

# Comando para ejecutar la API al iniciar el contenedor
CMD ["python", "DataReceiverAPI.py"]

