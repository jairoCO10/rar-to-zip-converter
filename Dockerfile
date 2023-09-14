FROM ubuntu:20.04

# Actualiza la lista de paquetes e instala unrar
RUN apt-get update && apt-get install -y unrar

# Instala Python y otras dependencias
RUN apt-get install -y python3 python3-pip

# Configura la ubicación de UnRAR para rarfile
ENV UNRAR_TOOL /usr/bin/unrar

# Establece el directorio de trabajo
WORKDIR /code

# Copia el archivo requirements.txt e instala las dependencias de Python
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia tu aplicación FastAPI al contenedor
COPY . /code

# Expone el puerto 80
EXPOSE 80

# Ejecuta la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# CMD ["python", "main.py"]

