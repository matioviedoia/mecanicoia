import os
import ast
import shutil
import datetime

BASE = "C:/IA/AGENTE/MECANICO"

def leer_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {e}"

def escribir_archivo(ruta, contenido):
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        return True
    except Exception:
        return False

def hacer_backup(ruta):
    if not os.path.isfile(ruta):
        return None
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = os.path.join(BASE, "memoria/backups", os.path.basename(ruta) + f".backup_{fecha}")
    os.makedirs(os.path.dirname(backup), exist_ok=True)
    shutil.copy2(ruta, backup)
    return backup

def validar_python(codigo):
    try:
        ast.parse(codigo)
        return True, "OK"
    except SyntaxError as e:
        return False, f"SyntaxError linea {e.lineno}: {e.msg}"

def extraer_codigo(texto):
    if "```python" in texto:
        inicio = texto.find("```python") + 9
        fin = texto.find("```", inicio)
        if fin > inicio:
            return texto[inicio:fin].strip()
    if "```" in texto:
        inicio = texto.find("```") + 3
        fin = texto.find("```", inicio)
        if fin > inicio:
            return texto[inicio:fin].strip()
    return texto.strip()

def hacer_prompt_reparacion(ruta, codigo):
    return (
        "Sos un experto en Python. Analizá este codigo y devolvé SOLO el codigo corregido.\n"
        "Corregi todos los errores, bugs y problemas de calidad.\n"
        "Mantene la funcionalidad original intacta.\n"
        "IMPORTANTE: Devolvé SOLO el codigo Python completo entre triple backticks.\n"
        "No agregues explicaciones ni comentarios fuera del codigo.\n\n"
        f"Archivo: {ruta}\n\n"
        f"```python\n{codigo[:4000]}\n```\n\n"
        "Devolvé SOLO el codigo corregido:"
    )

def reparar_archivo(ruta, preguntar_fn):
    if not os.path.exists(ruta):
        return f"ERROR: Archivo no encontrado: {ruta}"

    codigo_original = leer_archivo(ruta)
    if codigo_original.startswith("ERROR"):
        return codigo_original

    log = []
    log.append(f"Reparando: {ruta}")

    # Intentar con hasta 3 APIs diferentes
    from config import APIS
    apis_orden = ["groq", "gemini", "cerebras", "zai", "ollama"]
    apis_activas = [a for a in apis_orden if a in APIS and APIS[a]["activa"] and (APIS[a]["key"] or a == "ollama")]

    codigo_nuevo = None
    api_usada = None

    for api in apis_activas:
        log.append(f"Consultando {api}...")
        try:
            respuesta = preguntar_fn(hacer_prompt_reparacion(ruta, codigo_original), api=api)
            codigo_candidato = extraer_codigo(respuesta)

            if not codigo_candidato:
                log.append(f"  {api}: no devolvio codigo")
                continue

            if ruta.endswith(".py"):
                valido, msg = validar_python(codigo_candidato)
                if not valido:
                    log.append(f"  {api}: codigo invalido - {msg}")
                    continue
                log.append(f"  {api}: codigo valido")

            codigo_nuevo = codigo_candidato
            api_usada = api
            break

        except Exception as e:
            log.append(f"  {api}: error - {e}")
            continue

    if not codigo_nuevo:
        return "\n".join(log) + "\nERROR: Ninguna API pudo generar codigo valido"

    log.append(f"Codigo valido generado por {api_usada}, haciendo backup...")
    backup = hacer_backup(ruta)
    if backup:
        log.append(f"Backup: {backup}")

    try:
        from modulos import git_manager
        git_result = git_manager.commit_automatico(f"MECANICO pre-reparacion: {os.path.basename(ruta)}")
        log.append(f"Git: {git_result}")
    except Exception:
        pass

    ok = escribir_archivo(ruta, codigo_nuevo)
    if not ok:
        return "\n".join(log) + "\nERROR: No se pudo escribir el archivo"

    log.append("Archivo reparado exitosamente")

    try:
        from modulos import git_manager
        git_result = git_manager.commit_automatico(f"MECANICO reparacion [{api_usada}]: {os.path.basename(ruta)}")
        log.append(f"Git commit: {git_result}")
    except Exception:
        pass

    log.append(f"Lineas originales: {len(codigo_original.splitlines())}")
    log.append(f"Lineas nuevas: {len(codigo_nuevo.splitlines())}")

    return "\n".join(log)

def ejecutar(accion, texto):
    palabras = texto.split()
    ruta = palabras[-1] if len(palabras) > 1 else ""

    if not ruta or not os.path.exists(ruta):
        return f"ERROR: Especifica la ruta. Ej: reparar C:/ruta/archivo.py"

    from mecanico import preguntar
    return reparar_archivo(ruta, preguntar)
