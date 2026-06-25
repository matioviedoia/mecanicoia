import os
import logging
from pathlib import Path
from typing import Callable, Optional

# --- Configuración de Logging ---
# Se configura un logger básico para registrar eventos y errores.
# Esto mejora la depuración y la visibilidad del flujo del programa.
logger = logging.getLogger(__name__)
# Se establece el nivel de logging a INFO. Cambiar a DEBUG para más detalles.
logger.setLevel(logging.INFO)
# Un handler para enviar logs a la consola.
handler = logging.StreamHandler()
# Un formateador para los mensajes de log.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# Se añade el handler al logger.
logger.addHandler(handler)
# --- Fin Configuración de Logging ---

# 7. Importación condicional: Se mueve la importación de `mecanico.preguntar` al principio del archivo.
# Esto mejora la legibilidad y asegura que la dependencia se resuelva al inicio.
# Se añade un bloque try-except para manejar el caso de que el módulo 'mecanico' no esté disponible.
try:
    from mecanico import preguntar
    logger.info("Módulo 'mecanico.preguntar' cargado exitosamente.")
except ImportError:
    logger.error("No se pudo importar 'preguntar' del módulo 'mecanico'. "
                 "Asegúrate de que el módulo 'mecanico' esté disponible y 'preguntar' sea accesible.")
    # Se define una función simulada para evitar un fallo total si 'preguntar' no se carga,
    # permitiendo que otras partes del código funcionen si no dependen directamente de ello.
    # La función `ejecutar` manejará este caso más adelante.
    preguntar: Optional[Callable[[str], str]] = None
except Exception as e:
    logger.error(f"Error inesperado al importar 'preguntar' de 'mecanico': {e}")
    preguntar = None


# 9. Nombre de funciones: La función `leer_y_preguntar` ha sido renombrada a `leer_archivo_y_realizar_pregunta`
# para mayor claridad, siguiendo la sugerencia. La función `ejecutar` ha sido actualizada
# internamente para llamar a esta nueva función, manteniendo su interfaz externa.
def leer_archivo_y_realizar_pregunta(
    ruta: str,
    pregunta: str,
    preguntar_fn: Callable[[str], str],
    max_lineas_contexto: int = 200
) -> str:
    """
    Lee el contenido de un archivo (con un límite configurable de líneas) y formula una pregunta
    basada en su contenido, utilizando una función de consulta proporcionada.

    Esta función mejora la robustez mediante validaciones de parámetros, manejo de errores
    más detallado y lectura eficiente de archivos.

    Args:
        ruta (str): La ruta del archivo a leer. Debe ser una cadena no vacía y apuntar a un archivo existente.
        pregunta (str): La pregunta que se desea formular sobre el contenido del archivo.
                        Debe ser una cadena no vacía.
        preguntar_fn (Callable[[str], str]): Una función callable (ej. un modelo de lenguaje)
                                             que toma un string (el prompt) y devuelve un string (la respuesta).
                                             Este parámetro es obligatorio y no puede ser None.
        max_lineas_contexto (int): El número máximo de líneas del archivo a incluir en el contexto
                                   enviado a `preguntar_fn`. Esto ayuda a gestionar el tamaño de entrada
                                   para modelos de lenguaje. Por defecto es 200 líneas.

    Returns:
        str: La respuesta generada por `preguntar_fn` basada en el prompt,
             o un mensaje de error descriptivo si ocurre algún problema durante el proceso
             (ej. archivo no encontrado, errores de lectura, parámetros inválidos).
    """
    # 1. Validación de parámetros y 2. Manejo de errores (TypeError)
    # Se verifica que los parámetros `ruta` y `pregunta` sean cadenas válidas y no estén vacías.
    if not isinstance(ruta, str) or not ruta.strip():
        logger.error(f"Error de validación: El parámetro 'ruta' es inválido o vacío: '{ruta}'")
        return "ERROR: La ruta del archivo no puede ser vacía o inválida."
    if not isinstance(pregunta, str) or not pregunta.strip():
        logger.error(f"Error de validación: El parámetro 'pregunta' es inválido o vacío: '{pregunta}'")
        return "ERROR: La pregunta no puede ser vacía o inválida."
    # 11. Comprobación de `None`: Se confía en el tipado (`Callable`) y en que Python lanzará un TypeError
    # si se intenta llamar a un objeto que no es callable (incluyendo `None`) en tiempo de ejecución.

    # 10. Tipado: Se han añadido los tipos a los parámetros y el valor de retorno.
    # 9. Nombres de variables: `ruta_path` es más descriptivo.
    ruta_path = Path(ruta)

    # 8. Comprobación de ruta: Se usa `is_file()` para asegurar que la ruta es un archivo, no un directorio.
    if not ruta_path.is_file():
        logger.error(f"Error de archivo: La ruta '{ruta_path}' no es un archivo válido o no existe.")
        return f"ERROR: Archivo no encontrado o no es un archivo válido: {ruta_path}"

    contenido_lineas: list[str] = []
    lineas_totales = 0
    try:
        # 3. Lectura de archivo: Se lee el archivo línea por línea para optimizar la memoria
        # con archivos grandes, en lugar de leer todo el contenido de una vez.
        # 4. Codificación: Se mantiene `errors="replace"` y se añade manejo específico de `UnicodeDecodeError`.
        with ruta_path.open("r", encoding="utf-8", errors="replace") as f:
            for i, linea in enumerate(f):
                # 5. Límite de líneas: El límite es configurable mediante `max_lineas_contexto`.
                if i < max_lineas_contexto:
                    contenido_lineas.append(linea.rstrip('\n'))  # Elimina el salto de línea para procesamiento consistente
                lineas_totales += 1
    except FileNotFoundError:
        # Aunque `is_file()` ya debería haberlo capturado, es una buena práctica por si acaso.
        logger.exception(f"Error inesperado: Archivo no encontrado para la ruta '{ruta_path}' durante la lectura.")
        return f"ERROR: Archivo no encontrado: {ruta_path}"
    except PermissionError as e:
        logger.exception(f"Error de permisos al leer el archivo '{ruta_path}': {e}")
        return f"ERROR: Permiso denegado para leer el archivo: {ruta_path}"
    except OSError as e:
        logger.exception(f"Error del sistema operativo al leer el archivo '{ruta_path}': {e}")
        return f"ERROR: Error del sistema operativo al leer el archivo: {e}"
    except UnicodeDecodeError as e:
        # Esto debería ser mitigado por `errors="replace"`, pero un catch explícito es útil.
        logger.exception(f"Error de codificación al leer el archivo '{ruta_path}': {e}")
        return f"ERROR: Error de codificación al leer el archivo (se utilizó 'replace'): {e}"
    except Exception as e:
        logger.exception(f"Ocurrió un error inesperado al leer el archivo '{ruta_path}': {e}")
        return f"ERROR: Error inesperado al leer el archivo: {e}"

    contenido_recortado = "\n".join(contenido_lineas)
    if lineas_totales > max_lineas_contexto:
        contenido_recortado += (f"\n...({lineas_totales} líneas totales, "
                                f"mostrando las primeras {max_lineas_contexto})")

    prompt = f"""Analiza este archivo y responde en español.
Archivo: {ruta_path}
Pregunta: {pregunta}

Contenido:
{contenido_recortado}

Responde directamente a la pregunta basándote en el contenido real del archivo."""

    logger.debug(f"Prompt generado para 'preguntar_fn':\n{prompt}")
    try:
        return preguntar_fn(prompt)
    except Exception as e:
        logger.exception(f"Error al ejecutar la función 'preguntar_fn' con el prompt.")
        return f"ERROR: Fallo al procesar la pregunta: {e}"


# CRITICO: La función `ejecutar` DEBE mantenerse exactamente igual en su nombre y firma.
# 6. Organización del código: Su implementación interna se ha mejorado para usar la función
# `leer_archivo_y_realizar_pregunta` y para ser más robusta.
def ejecutar(accion: str, texto: str) -> str:
    """
    Ejecuta la acción de leer y preguntar sobre un archivo.
    Este es el punto de entrada principal para acciones relacionadas con la lectura de contexto.
    Parsea el texto de entrada para extraer la ruta del archivo y la pregunta,
    y luego utiliza la funcionalidad de lectura de archivo y pregunta.

    Args:
        accion (str): La acción a realizar. Se espera que sea "leer". Este parámetro
                      se usa para el logging pero no para la lógica principal.
        texto (str): El texto de entrada que contiene la ruta del archivo y la pregunta,
                     siguiendo el formato "leer C:/ruta/archivo.js y qué hace este código".

    Returns:
        str: La respuesta a la pregunta obtenida del procesador de lenguaje (via `preguntar_fn`),
             o un mensaje de error si la entrada es inválida o el procesamiento falla.
    """
    logger.info(f"Ejecutando la acción '{accion}' con el texto: '{texto}'")

    # Se mantiene la lógica de parsing original para preservar la funcionalidad exacta.
    partes = texto.split(" y ", 1)
    if len(partes) < 2:
        partes = texto.split(" para ", 1)
    if len(partes) < 2:
        logger.warning(f"Formato de entrada incorrecto para 'ejecutar'. Texto recibido: '{texto}'")
        return "ERROR: Uso: leer C:/ruta/archivo.js y qué hace este código"

    ruta_parte = partes[0].replace("leer ", "").strip()
    # 9. Nombres de variables: `pregunta_texto` es más descriptivo para evitar conflictos.
    pregunta_texto = partes[1].strip()

    # Se verifica si la función `preguntar` fue importada exitosamente al inicio del script.
    if preguntar is None:
        logger.error("La función 'preguntar' de 'mecanico' no está disponible. No se puede proceder.")
        return "ERROR: La funcionalidad de pregunta no está disponible (módulo 'mecanico' no cargado o falló)."

    # Se llama a la función de lectura y pregunta mejorada, pasando `preguntar` como callable.
    return leer_archivo_y_realizar_pregunta(ruta_parte, pregunta_texto, preguntar)