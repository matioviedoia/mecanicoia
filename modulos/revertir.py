import os
import shutil
import glob
from typing import List

BASE: str = os.environ.get('BASE_DIR', "C:/IA/AGENTE/MECANICO")
BACKUPS: str = os.path.join(BASE, "memoria", "backups")

def listar_backups(archivo: str) -> List[str]:
    """
    Lista los backups de un archivo.

    Args:
    archivo (str): Ruta del archivo.

    Returns:
    List[str]: Lista de nombres de los backups del archivo.
    """
    if not archivo:
        raise ValueError("El archivo no puede ser vacío")

    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        raise ValueError(f"No hay backups de {nombre}")

    return [os.path.basename(b) for b in backups[:5]]

def revertir(archivo: str) -> str:
    """
    Revierte un archivo a su versión más reciente.

    Args:
    archivo (str): Ruta del archivo.

    Returns:
    str: Mensaje de confirmación de la reversión.
    """
    if not archivo:
        raise ValueError("El archivo no puede ser vacío")

    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        raise ValueError(f"No hay backups de {nombre}")

    backup_reciente = backups[0]
    ruta_destino = os.path.abspath(archivo)
    try:
        shutil.copy2(backup_reciente, ruta_destino)
        return f"OK Revertido a: {os.path.basename(backup_reciente)}\nArchivo restaurado: {ruta_destino}"
    except Exception as e:
        raise ValueError(f"Error al revertir el archivo: {e}")

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
        return "\n".join(listar_backups(archivo))
    return revertir(archivo)

def main():
    accion = input("Ingrese la acción (listar o revertir): ")
    archivo = input("Ingrese la ruta del archivo: ")
    if accion.lower() == "listar":
        try:
            backups = listar_backups(archivo)
            print("Backups del archivo:")
            for backup in backups:
                print(backup)
        except ValueError as e:
            print(e)
    elif accion.lower() == "revertir":
        try:
            resultado = revertir(archivo)
            print(resultado)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()