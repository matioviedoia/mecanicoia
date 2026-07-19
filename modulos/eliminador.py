import os
import shutil
import datetime
import logging

# Configuración del log
logging.basicConfig(level=logging.INFO)

# Constantes
KEYWORDS = ["borrar", "eliminar", "delete", "eliminador"]
FECHA_HORA_FORMATO = "%Y%m%d%H%M%S"

def crear_directorio(directorio: str) -> None:
    """
    Crea un directorio si no existe.
    
    Args:
        directorio (str): Ruta del directorio a crear.
    """
    try:
        os.makedirs(directorio, exist_ok=True)
    except OSError as e:
        logging.error(f"Error al crear directorio {directorio}: {e}")

def crear_backup(archivo: str) -> str:
    """
    Crea una copia de seguridad de un archivo.
    
    Args:
        archivo (str): Ruta del archivo a crear backup.
    
    Returns:
        str: Ruta del archivo de backup.
    
    Raises:
        FileNotFoundError: Si el archivo no existe.
        PermissionError: Si no se tiene permiso para leer el archivo.
    """
    try:
        # Obtener la fecha y hora actuales
        timestamp = datetime.datetime.now().strftime(FECHA_HORA_FORMATO)
        
        # Crear la ruta del archivo de backup
        nombre_archivo = os.path.basename(archivo)
        directorio_archivo = os.path.dirname(archivo)
        nombre_backup = f"backup_{nombre_archivo}_{timestamp}"
        ruta_backup = os.path.join(directorio_archivo, "backups", nombre_backup)
        
        # Crear el directorio de backups si no existe
        directorio_backups = os.path.dirname(ruta_backup)
        crear_directorio(directorio_backups)
        
        # Copiar el archivo original al archivo de backup
        shutil.copy2(archivo, ruta_backup)
        
        return ruta_backup
    
    except FileNotFoundError:
        logging.error(f"El archivo {archivo} no existe")
        raise
    except PermissionError:
        logging.error(f"No se tiene permiso para leer el archivo {archivo}")
        raise
    except Exception as e:
        logging.error(f"Error al crear backup: {e}")
        raise

def borrar_archivo(archivo: str) -> str:
    """
    Borra un archivo de forma segura.
    
    Args:
        archivo (str): Ruta del archivo a borrar.
    
    Returns:
        str: Confirmación del backup creado y la ruta borrada.
    
    Raises:
        FileNotFoundError: Si el archivo no existe.
    """
    try:
        # Verificar que el archivo exista
        if not os.path.exists(archivo):
            raise FileNotFoundError(f"El archivo {archivo} no existe")
        
        # Crear una copia de seguridad del archivo
        ruta_backup = crear_backup(archivo)
        
        # Borrar el archivo original
        os.remove(archivo)
        
        return f"Archivo {archivo} borrado con éxito. Backup creado en {ruta_backup}"
    
    except Exception as e:
        logging.error(f"Error al borrar archivo: {e}")
        raise

def ejecutar(accion: str, texto: str) -> str:
    """
    Interpretar el texto y llamar a las funciones del módulo.
    
    Args:
        accion (str): Acción a realizar.
        texto (str): Texto a interpretar.
    
    Returns:
        str: Resultado de la acción.
    """
    if not any(palabra in texto.lower() for palabra in KEYWORDS):
        return "Acción no soportada."

    # Completar la lógica para obtener la ruta del archivo a borrar
    archivo = texto.split()[-1]
    try:
        return borrar_archivo(archivo)
    except Exception as e:
        logging.error(f"Error al ejecutar acción: {e}")
        raise