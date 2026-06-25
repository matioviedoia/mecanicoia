import os
from pathlib import Path
from typing import Callable

def leer_y_preguntar(ruta: str, pregunta: str, preguntar_fn: Callable[[str], str]) -> str:
    """
    Lee el contenido de un archivo y pregunta sobre su contenido.

    Args:
    ruta (str): La ruta del archivo a leer.
    pregunta (str): La pregunta sobre el contenido del archivo.
    preguntar_fn (Callable[[str], str]): La función para realizar la pregunta.

    Returns:
    str: La respuesta a la pregunta.
    """
    ruta = Path(ruta)
    if not ruta.exists():
        return f"ERROR: Archivo no encontrado: {ruta}"
    try:
        with ruta.open("r", encoding="utf-8", errors="replace") as f:
            contenido = f.read()
    except OSError as e:
        return f"ERROR leyendo archivo: {e}"
    except UnicodeDecodeError as e:
        return f"ERROR leyendo archivo: {e}"
    lineas = contenido.splitlines()
    if len(lineas) > 200:
        contenido_recortado = "\n".join(lineas[:200]) + f"\n...({len(lineas)} líneas totales, mostrando las primeras 200)"
    else:
        contenido_recortado = contenido
    prompt = f"""Analiza este archivo y responde en español.
Archivo: {ruta}
Pregunta: {pregunta}

Contenido:
{contenido_recortado}

Responde directamente a la pregunta basándote en el contenido real del archivo."""
    if preguntar_fn is None:
        raise ValueError("La función preguntar_fn no puede ser None")
    return preguntar_fn(prompt)

def ejecutar(accion: str, texto: str) -> str:
    """
    Ejecuta la acción de leer y preguntar sobre un archivo.

    Args:
    accion (str): La acción a realizar.
    texto (str): El texto con la ruta y la pregunta.

    Returns:
    str: La respuesta a la pregunta.
    """
    partes = texto.split(" y ", 1)
    if len(partes) < 2:
        partes = texto.split(" para ", 1)
    if len(partes) < 2:
        return "ERROR: Uso: leer C:/ruta/archivo.js y qué hace este código"
    ruta_parte = partes[0].replace("leer ", "").strip()
    pregunta = partes[1].strip()
    from mecanico import preguntar
    return leer_y_preguntar(ruta_parte, pregunta, preguntar)