from fastapi import FastAPI, File, UploadFile
import rarfile
import zipfile
import shutil
import os
from fastapi.responses import FileResponse

from  src.controller import Convertir
app = FastAPI()

@app.post("/convert/")
async def convert_to_zip(file: UploadFile):
    # Verificar si es un archivo RAR
    convertir =Convertir()
    archivo_zip = convertir.convert_file(file)

    return FileResponse(archivo_zip, media_type='application/zip', filename=archivo_zip)
