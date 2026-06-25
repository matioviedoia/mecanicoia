import os
from pathlib import Path

BASE = Path("C:/IA/AGENTE/MECANICO")

def leer_y_preguntar(ruta, pregunta, preguntar_fn):
    """Lee el contenido de un archivo y pregunta sobre su contenido."""
    ruta = Path(ruta)
    if not ruta.exists():
        return f"ERROR: Archivo no encontrado: {ruta}"
    try:
        with ruta.open("r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
    except Exception as e:
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
    return preguntar_fn(prompt)

def ejecutar(accion, texto):
    """Ejecuta la acción de leer y preguntar sobre un archivo."""
    partes = texto.split(" y ", 1)
    if len(partes) < 2:
        partes = texto.split(" para ", 1)
    if len(partes) < 2:
        return "ERROR: Uso: leer C:/ruta/archivo.js y qué hace este código"
    ruta_parte = partes[0].replace("leer ", "").strip()
    pregunta = partes[1].strip()
    from mecanico import preguntar
    return leer_y_preguntar(ruta_parte, pregunta, preguntar)