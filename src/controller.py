import rarfile
import zipfile
import shutil
import os

class Convertir:
    def convert_file(self, file):
        if not file.filename.endswith(".rar"):
            return {"error": "El archivo debe tener extensión .rar"}

        # Crear una carpeta temporal para almacenar los archivos descomprimidos
        temp_folder = "temp_folder"
        os.makedirs(temp_folder, exist_ok=True)

        # Guardar el archivo RAR en la carpeta temporal
        with open(os.path.join(temp_folder, file.filename), "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Descomprimir el archivo RAR
        with rarfile.RarFile(os.path.join(temp_folder, file.filename), 'r') as rf:
            rf.extractall(temp_folder)

        # Crear un archivo ZIP a partir de los archivos descomprimidos
        archivo_zip = os.path.splitext(file.filename)[0] + ".zip"
        with zipfile.ZipFile(archivo_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(temp_folder):
                for archivo in files:
                    ruta_completa = os.path.join(root, archivo)
                    arcname = os.path.relpath(ruta_completa, temp_folder)
                    zf.write(ruta_completa, arcname)

        # Eliminar la carpeta temporal
        shutil.rmtree(temp_folder)


        return archivo_zip