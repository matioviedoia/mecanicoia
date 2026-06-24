import os

BASE = "C:/IA/AGENTE/MECANICO"

def leer_y_preguntar(ruta, pregunta, preguntar_fn):
    if not os.path.exists(ruta):
        return f"ERROR: Archivo no encontrado: {ruta}"
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
    except Exception as e:
        return f"ERROR leyendo archivo: {e}"
    lineas = contenido.split("\n")
    if len(lineas) > 200:
        contenido_recortado = "\n".join(lineas[:200]) + f"\n...({len(lineas)} lineas total, mostrando primeras 200)"
    else:
        contenido_recortado = contenido
    prompt = f"""Analizá este archivo y respondes en espanol.
Archivo: {ruta}
Pregunta: {pregunta}

Contenido:
{contenido_recortado}

Responde directamente a la pregunta basandote en el contenido real del archivo."""
    return preguntar_fn(prompt)

def ejecutar(accion, texto):
    partes = texto.split(" y ", 1)
    if len(partes) < 2:
        partes = texto.split(" para ", 1)
    if len(partes) < 2:
        return "ERROR: Uso: leer C:/ruta/archivo.js y que hace este codigo"
    ruta_parte = partes[0].replace("leer ", "").strip()
    pregunta = partes[1].strip()
    from mecanico import preguntar
    return leer_y_preguntar(ruta_parte, pregunta, preguntar)
