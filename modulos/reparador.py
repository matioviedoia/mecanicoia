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

def validar_modulo(codigo_nuevo, codigo_original):
    if "def ejecutar(" not in codigo_nuevo and "def ejecutar(" in codigo_original:
        return False, "ERROR: La funcion ejecutar fue eliminada"
    return True, "OK"

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

def intentar_con_apis(prompt, preguntar_fn, ruta, codigo_original=""):
    from config import APIS
    apis_orden = ["groq", "gemini", "cerebras", "zai", "ollama"]
    apis_activas = [a for a in apis_orden if a in APIS and APIS[a]["activa"] and (APIS[a]["key"] or a == "ollama")]

    for api in apis_activas:
        try:
            respuesta = preguntar_fn(prompt, api=api)
            codigo_candidato = extraer_codigo(respuesta)
            if not codigo_candidato:
                continue
            if ruta.endswith(".py"):
                valido, msg = validar_python(codigo_candidato)
                if not valido:
                    continue
                if codigo_original:
                    valido, msg = validar_modulo(codigo_candidato, codigo_original)
                    if not valido:
                        continue
            return codigo_candidato, api
        except Exception:
            continue
    return None, None

def guardar_git(mensaje):
    try:
        from modulos import git_manager
        return git_manager.commit_automatico(mensaje)
    except Exception:
        return None

def procesar(ruta, preguntar_fn, modo="reparar"):
    if not os.path.exists(ruta):
        return f"ERROR: Archivo no encontrado: {ruta}"

    codigo_original = leer_archivo(ruta)
    if codigo_original.startswith("ERROR"):
        return codigo_original

    log = []
    log.append(f"{'Reparando' if modo == 'reparar' else 'Mejorando'}: {ruta}")

    if modo == "reparar":
        prompt = (
            "Sos un experto en Python. Analizá este codigo y devolvé SOLO el codigo corregido.\n"
            "Corregi todos los errores, bugs y problemas de calidad.\n"
            "Mantene la funcionalidad original intacta.\n"
            "CRITICO: Si el codigo tiene una funcion llamada ejecutar, DEBES mantenerla exactamente igual.\n"
            "IMPORTANTE: Devolvé SOLO el codigo Python completo entre triple backticks.\n"
            "No agregues explicaciones fuera del codigo.\n\n"
            f"Archivo: {ruta}\n\n"
            f"```python\n{codigo_original[:4000]}\n```\n\n"
            "Devolvé SOLO el codigo corregido:"
        )
    else:
        log.append("Analizando para obtener sugerencias de mejora...")
        prompt_analisis = (
            "Analizá este codigo Python y listá de forma concisa las mejoras que aplicarías.\n"
            "Sé específico y técnico.\n\n"
            f"```python\n{codigo_original[:3000]}\n```"
        )
        sugerencias, _ = intentar_con_apis(prompt_analisis, preguntar_fn, "")
        if not sugerencias:
            sugerencias = "mejorar manejo de errores, eliminar codigo duplicado, agregar documentacion"
        log.append(f"Sugerencias: {sugerencias[:200]}...")

        prompt = (
            "Sos un experto en Python. Mejorá este codigo aplicando las siguientes sugerencias.\n"
            "Mantene la funcionalidad original pero mejora la calidad, estructura y rendimiento.\n"
            "CRITICO: Si el codigo tiene una funcion llamada ejecutar, DEBES mantenerla exactamente igual.\n"
            "IMPORTANTE: Devolvé SOLO el codigo Python completo mejorado entre triple backticks.\n"
            "No agregues explicaciones fuera del codigo.\n\n"
            f"Sugerencias a aplicar:\n{sugerencias}\n\n"
            f"Archivo: {ruta}\n\n"
            f"```python\n{codigo_original[:3000]}\n```\n\n"
            "Devolvé SOLO el codigo mejorado:"
        )

    log.append("Consultando APIs...")
    codigo_nuevo, api_usada = intentar_con_apis(prompt, preguntar_fn, ruta, codigo_original)

    if not codigo_nuevo:
        return "\n".join(log) + "\nERROR: Ninguna API pudo generar codigo valido"

    log.append(f"Codigo valido generado por {api_usada}")

    backup = hacer_backup(ruta)
    if backup:
        log.append(f"Backup: {backup}")

    guardar_git(f"MECANICO pre-{modo}: {os.path.basename(ruta)}")

    ok = escribir_archivo(ruta, codigo_nuevo)
    if not ok:
        return "\n".join(log) + "\nERROR: No se pudo escribir el archivo"

    log.append(f"Archivo {modo}do exitosamente")
    guardar_git(f"MECANICO {modo} [{api_usada}]: {os.path.basename(ruta)}")

    log.append(f"Lineas originales: {len(codigo_original.splitlines())}")
    log.append(f"Lineas nuevas: {len(codigo_nuevo.splitlines())}")

    return "\n".join(log)

def ejecutar(accion, texto):
    palabras = texto.split()
    ruta = palabras[-1] if len(palabras) > 1 else ""

    if not ruta or not os.path.exists(ruta):
        return f"ERROR: Especifica la ruta. Ej: reparar C:/ruta/archivo.py"

    from mecanico import preguntar

    if accion == "mejorar":
        return procesar(ruta, preguntar, modo="mejorar")
    else:
        return procesar(ruta, preguntar, modo="reparar")
