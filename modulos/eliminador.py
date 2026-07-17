import os
import shutil
import datetime
import json

# Lista de palabras clave
KEYWORDS = ["borrar", "eliminar", "delete"]

def crear_backup(archivo):
    """
    Crea una copia de seguridad de un archivo.
    
    Args:
        archivo (str): Ruta del archivo a crear backup.
    
    Returns:
        str: Ruta del archivo de backup.
    """
    try:
        # Obtener la fecha y hora actuales
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Crear la ruta del archivo de backup
        nombre_archivo = os.path.basename(archivo)
        directorio_archivo = os.path.dirname(archivo)
        nombre_backup = f"backup_{nombre_archivo}_{timestamp}"
        ruta_backup = os.path.join(directorio_archivo, "backups", nombre_backup)
        
        # Crear el directorio de backups si no existe
        directorio_backups = os.path.dirname(ruta_backup)
        if not os.path.exists(directorio_backups):
            os.makedirs(directorio_backups)
        
        # Copiar el archivo original al archivo de backup
        shutil.copy(archivo, ruta_backup)
        
        return ruta_backup
    
    except Exception as e:
        print(f"Error al crear backup: {e}")
        return None

def borrar_archivo(archivo):
    """
    Borra un archivo de forma segura.
    
    Args:
        archivo (str): Ruta del archivo a borrar.
    
    Returns:
        str: Confirmación del backup creado y la ruta borrada.
    """
    try:
        # Verificar que el archivo exista
        if not os.path.exists(archivo):
            return f"Error: El archivo {archivo} no existe."
        
        # Crear una copia de seguridad del archivo
        ruta_backup = crear_backup(archivo)
        if ruta_backup is None:
            return "Error al crear backup."
        
        # Borrar el archivo original
        os.remove(archivo)
        
        return f"Archivo {archivo} borrado con éxito. Backup creado en {ruta_backup}"
    
    except Exception as e:
        print(f"Error al borrar archivo: {e}")
        return "Error al borrar archivo."

def ejecutar(accion, texto):
    """
    Interpretar el texto y llamar a las funciones del módulo.
    
    Args:
        accion (str): Acción a realizar.
        texto (str): Texto a interpretar.
    
    Returns:
        str: Resultado de la acción.
    """
    try:
        # Verificar que la acción sea borrar
        if accion.lower() not in KEYWORDS:
            return "Acción no soportada."
        
        # Obtener la ruta del archivo a borrar
        archivo = texto.strip()
        
        # Borrar el archivo
        resultado = borrar_archivo(archivo)
        
        return resultado
    
    except Exception as e:
        print(f"Error al ejecutar acción: {e}")
        return "Error al ejecutar acción."