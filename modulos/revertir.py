import os
import shutil
import glob

BASE = "C:/IA/AGENTE/MECANICO"
BACKUPS = os.path.join(BASE, "memoria", "backups")

def listar_backups(archivo):
    """
    Lista los backups de un archivo.
    
    Parametros:
    archivo (str): Ruta del archivo.
    
    Retorno:
    str: Lista de backups del archivo.
    """
    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        return f"No hay backups de {nombre}"
    resultado = f"Backups de {nombre}:\n"
    for i, b in enumerate(backups[:5], start=1):
        resultado += f"  {i}. {os.path.basename(b)}\n"
    return resultado

def revertir(archivo):
    """
    Revierte un archivo a su versión más reciente.
    
    Parametros:
    archivo (str): Ruta del archivo.
    
    Retorno:
    str: Mensaje de confirmación de la reversión.
    """
    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        return f"ERROR: No hay backups de {nombre}"
    backup_reciente = backups[0]
    if os.path.isabs(archivo):
        ruta_destino = archivo
    else:
        ruta_destino = os.path.join(BASE, archivo)
    try:
        shutil.copy2(backup_reciente, ruta_destino)
        return f"OK Revertido a: {os.path.basename(backup_reciente)}\nArchivo restaurado: {ruta_destino}"
    except OSError as e:
        return f"ERROR: {e}"

def ejecutar(accion, texto):
    """
    Ejecuta una acción sobre un archivo.
    
    Parametros:
    accion (str): Acción a realizar.
    texto (str): Texto que contiene la ruta del archivo.
    
    Retorno:
    str: Mensaje de confirmación o error.
    """
    palabras = texto.split()
    archivo = palabras[-1] if len(palabras) > 1 else ""
    if not archivo:
        return "ERROR: Especifica el archivo. Ej: revertir mecanico.py"
    if "listar" in texto.lower():
        return listar_backups(archivo)
    return revertir(archivo)