import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
KEYWORDS = ["github leer", "github reader", "leer repo", "analizar repo"]

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

EXTENSIONES_UTILES = [".py", ".md", ".txt", ".js", ".json", ".yaml", ".yml"]
IGNORAR_CARPETAS = ["node_modules", "__pycache__", ".git", "venv", "env", "dist", "build", "test", "tests"]
MAX_ARCHIVOS = 10
MAX_SIZE_ARCHIVO = 50000
MAX_TOTAL_CHARS = 15000
LIMITE_REPO_PEQUEÑO_ARCHIVOS = 5
LIMITE_REPO_PEQUEÑO_KB = 20000

def parsear_url(url):
    url = url.replace("https://github.com/", "").strip("/")
    partes = url.split("/")
    if len(partes) >= 2:
        return partes[0], partes[1]
    return None, None

def listar_archivos(owner, repo, path=""):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return []
        archivos = []
        for item in r.json():
            if item["type"] == "dir":
                if item["name"] not in IGNORAR_CARPETAS:
                    archivos.extend(listar_archivos(owner, repo, item["path"]))
            elif item["type"] == "file":
                ext = os.path.splitext(item["name"])[1].lower()
                if ext in EXTENSIONES_UTILES and item["size"] < MAX_SIZE_ARCHIVO:
                    archivos.append(item)
        return archivos
    except Exception:
        return []

def leer_archivo_github(owner, repo, path):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return None
        data = r.json()
        if data.get("encoding") == "base64":
            return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
        return None
    except Exception:
        return None

def resumir_archivo(nombre, contenido, preguntar_fn):
    ext = os.path.splitext(nombre)[1].lower()
    if ext == ".md" and nombre.lower() == "readme.md":
        max_palabras = 200
    elif ext == ".py" and ("main" in nombre.lower() or "__init__" in nombre.lower()):
        max_palabras = 100
    elif ext in [".txt", ".yaml", ".yml", ".json"]:
        max_palabras = 20
    else:
        max_palabras = 50
    contenido_corto = contenido[:3000]
    prompt = (
        f"Resume este archivo '{nombre}' en maximo {max_palabras} palabras en español.\n"
        "Incluye: que hace, funciones/clases clave, dependencias importantes.\n\n"
        f"{contenido_corto}"
    )
    try:
        return preguntar_fn(prompt, api="ollama")
    except Exception:
        return contenido[:200]

def es_repo_pequeño(archivos):
    archivos_py = [a for a in archivos if a["name"].endswith(".py")]
    total_size = sum(a["size"] for a in archivos)
    return len(archivos_py) <= LIMITE_REPO_PEQUEÑO_ARCHIVOS and total_size <= LIMITE_REPO_PEQUEÑO_KB

def implementar_directo(owner, repo, archivos, resumenes, preguntar_fn):
    log = []
    log.append("\nRepo pequeño detectado. Implementando directamente en MECANICO...\n")
    resumen_total = "\n\n".join(resumenes)
    prompt = (
        "Sos experto en Python. Basandote en este repo GitHub, crea un modulo Python\n"
        "que integre su funcionalidad en MECANICO, un agente que analiza y repara codigo.\n"
        "REGLAS:\n"
        "1. El modulo DEBE tener una funcion ejecutar(accion, texto) al final\n"
        "2. Debe tener una variable KEYWORDS con lista de palabras clave\n"
        "3. Usa solo librerias estandar o muy comunes\n"
        "4. Maneja todos los errores con try/except\n"
        "5. Devolvé SOLO el codigo Python entre triple backticks\n\n"
        f"REPO: {owner}/{repo}\n\n"
        f"{resumen_total[:4000]}"
    )
    codigo = None
    api_usada = None
    for api in ["gemini", "cerebras", "groq", "ollama"]:
        try:
            respuesta = preguntar_fn(prompt, api=api)
            if "```" in respuesta:
                inicio = respuesta.find("```python") + 9 if "```python" in respuesta else respuesta.find("```") + 3
                fin = respuesta.find("```", inicio)
                if fin > inicio:
                    codigo = respuesta[inicio:fin].strip()
                    api_usada = api
                    break
        except Exception:
            continue
    if not codigo:
        return "\nERROR: No se pudo generar el modulo"
    nombre_modulo = f"{repo.lower().replace('-', '_').replace('.', '_')}.py"
    ruta = f"C:/IA/AGENTE/MECANICO/modulos/{nombre_modulo}"
    try:
        import ast
        ast.parse(codigo)
    except SyntaxError as e:
        return f"\nERROR: Codigo generado invalido: {e}"
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(codigo)
    log.append(f"Modulo creado por {api_usada}: {ruta}")
    try:
        from modulos import autoeditor
        trigger = repo.lower().replace("-", "").replace("_", "")[:10]
        resultado_trigger = autoeditor.agregar_trigger(trigger, nombre_modulo.replace(".py", ""))
        log.append(resultado_trigger)
    except Exception as e:
        log.append(f"Trigger manual necesario: {e}")
    try:
        from modulos import git_manager
        git_manager.commit_automatico(f"MECANICO auto-integro repo: {owner}/{repo}")
        log.append("Git commit realizado")
    except Exception:
        pass
    log.append(f"\nOK Repo {owner}/{repo} integrado exitosamente")
    log.append("Escribi 'recargar' para cargar el nuevo modulo sin reiniciar")
    return "\n".join(log)

def analizar_repo(url_repo, preguntar_fn):
    owner, repo = parsear_url(url_repo)
    if not owner or not repo:
        return f"ERROR: URL invalida: {url_repo}"
    log = []
    log.append(f"Analizando repo: {owner}/{repo}\n")
    archivos = listar_archivos(owner, repo)
    if not archivos:
        return f"ERROR: No se pudieron listar archivos de {owner}/{repo}"
    archivos_ordenados = []
    for a in archivos:
        if a["name"].lower() == "readme.md":
            archivos_ordenados.insert(0, a)
        elif a["name"].endswith(".py"):
            archivos_ordenados.append(a)
    for a in archivos:
        if a not in archivos_ordenados:
            archivos_ordenados.append(a)
    top_archivos = archivos_ordenados[:MAX_ARCHIVOS]
    pequeño = es_repo_pequeño(archivos)
    log.append(f"Archivos encontrados: {len(archivos)}, analizando top {len(top_archivos)}")
    log.append(f"Tamaño: {'PEQUEÑO - implementacion automatica posible' if pequeño else 'GRANDE - solo sugerencias'}\n")
    resumenes = []
    total_chars = 0
    for archivo in top_archivos:
        if total_chars >= MAX_TOTAL_CHARS:
            break
        contenido = leer_archivo_github(owner, repo, archivo["path"])
        if not contenido:
            continue
        log.append(f"Resumiendo: {archivo['path']}...")
        resumen = resumir_archivo(archivo["name"], contenido, preguntar_fn)
        resumenes.append(f"### {archivo['path']}\n{resumen}")
        total_chars += len(resumen)
    if not resumenes:
        return "ERROR: No se pudo leer ningun archivo"
    resumen_total = "\n\n".join(resumenes)
    if pequeño:
        log.append(implementar_directo(owner, repo, archivos, resumenes, preguntar_fn))
        return "\n".join(log)
    log.append("\n" + resumen_total)
    prompt_final = (
        "Sos experto en agentes IA Python. Analiza este repo GitHub.\n"
        "Responde en español con estas 4 secciones:\n"
        "1. QUE HACE: descripcion clara (50 palabras)\n"
        "2. FUNCIONES UTILES: que podria integrarse en MECANICO (100 palabras)\n"
        "3. DEPENDENCIAS: librerias necesarias\n"
        "4. PLAN DE INTEGRACION: como crear el modulo (100 palabras)\n\n"
        f"REPO: {owner}/{repo}\n\n"
        f"{resumen_total[:5000]}"
    )
    log.append("\nAnalizando con Gemini...\n")
    analisis = None
    for api in ["gemini", "cerebras", "ollama"]:
        try:
            resultado = preguntar_fn(prompt_final, api=api)
            if resultado and "ERROR" not in resultado:
                analisis = f"[{api}]:\n{resultado}"
                break
        except Exception:
            continue
    log.append(analisis or "No se pudo analizar")
    return "\n".join(log)

def ejecutar(accion, texto):
    palabras = texto.split()
    url = next((p for p in palabras if "github.com" in p), None)
    if not url:
        return "ERROR: Especifica la URL. Ej: github leer https://github.com/usuario/repo"
    from mecanico import preguntar
    return analizar_repo(url, preguntar)
