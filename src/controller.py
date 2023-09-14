import rarfile
import zipfile
import shutil
import os

class Convertir:
    def convert_file(self, file):
        if not file.filename.endswith(".rar"):
            return {"error": "El archivo debe tener extensión .rar"}

        # Carpeta donde se almacenan los archivos temporales
        temp_folder = "uploads"
        os.makedirs(temp_folder, exist_ok=True)
        # Descomprimir el archivo RAR en la carpeta "downloads"
        download_folder = "downloads"
        os.makedirs(download_folder, exist_ok=True)

        # Guardar el archivo RAR en la carpeta temporal
        with open(os.path.join(temp_folder, file.filename), "wb") as f:
            shutil.copyfileobj(file.file, f)

        
        with rarfile.RarFile(os.path.join(temp_folder, file.filename), 'r') as rf:
            rf.extractall(download_folder)

        # Crear un archivo ZIP a partir de los archivos descomprimidos
        archivo_zip = os.path.join(download_folder, os.path.splitext(file.filename)[0] + ".zip")
        with zipfile.ZipFile(archivo_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(download_folder):
                for archivo in files:
                    ruta_completa = os.path.join(root, archivo)
                    arcname = os.path.relpath(ruta_completa, download_folder)
                    zf.write(ruta_completa, arcname)

        # Eliminar solo los archivos temporales, pero mantener la carpeta "uploads"
        # for archivo_temporal in os.listdir(temp_folder):
        #     archivo_temporal_path = os.path.join(temp_folder, archivo_temporal)
        #     if os.path.isfile(archivo_temporal_path):
        #         os.remove(archivo_temporal_path)

        return archivo_zip
