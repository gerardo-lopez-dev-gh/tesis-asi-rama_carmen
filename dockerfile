# Etapa 1: Construcción del binario
FROM python:3.10-slim AS builder

# Instalar las dependencias del sistema necesarias para compilar el binario
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo para la construcción
WORKDIR /build

# Copiar los archivos de dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pyinstaller

# Copiar todo el proyecto
COPY . .

# Construir el binario usando PyInstaller
RUN pyinstaller --onefile index.py

# Confirmar que el binario se generó correctamente
RUN ls -la /build/dist

# Etapa 2: Imagen de ejecución
FROM alpine:latest

# Crear un directorio de trabajo
WORKDIR /app

# Copiar el binario generado en la etapa de construcción
COPY --from=builder /build/dist/index /app/

# Verificar el contenido en la etapa de ejecución
RUN ls -la /app/

# Exponer el puerto de la aplicación
EXPOSE 5000

# Ejecutar el binario
CMD ["./index"]
