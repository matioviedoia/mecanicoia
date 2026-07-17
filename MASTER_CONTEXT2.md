# MASTER CONTEXT - MECANICO IA
Generado: 2026-07-09 23:03

## ESTRUCTURA
```
MECANICO/
  .env
  .gitignore
  analizador.py
  app.log
  config.py
  copiar_para_ia.py
  explorador.py
  generar_contexto.py
  historial.log
  MANUAL_MECANICO.md
  MASTER_CONTEXT.md
  MASTER_CONTEXT2.md
  mecanico.py
  orquestador.py
  scanner_maestro.py
  uptime.py
  apis/
  ENTORN VISUAL/
    CARETAS.BAT
    Nueva carpeta/
  logs/
    errors/
      errores.log
  memoria/
    historial.log
    token_log.json
    errores/
      errores.log
    sesiones/
  modulos/
    analizador.py
    autoeditor.py
    bucle_mejora.py
    buscador_web.py
    explorador.py
    generador.py
    github_reader.py
    github_scout.py
    git_manager.py
    lector_contexto.py
    memoria_historial.py
    nvidia_selector.py
    orquestador.py
    reinicio.py
    reparador.py
    revertir.py
    tester.py
    texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial.py
    token_monitor.py
    uptime.py
    Nueva carpeta/
      asfasf.py
      generador.py
      mecanico (1).py
      mecanico.py
      token_monitor.py
  proyectos/
  visual/
    assets/
      fonts/
      icons/
    components/
    css/
    data/
    js/
    logs/
    pages/
    templates/
    themes/
  workspace/
    limpiar.txt
    test.txt
    test_autoeditor.txt
```

## MODULOS

### analizador.py
```python
# Este módulo analiza código Python en busca de errores, advertencias y problemas de rendimiento, 
# y ofrece opciones para analizar archivos y proyectos utilizando técnicas de inteligencia artificial.

import os
import ast
import json

BASE = "C:/IA/AGENTE/MECANICO"

def leer_archivo(ruta: str) -> str:
    """Lee el contenido de un archivo."""
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {str(e)}"

def analizar_python(ruta: str) -> str:
    """Analiza un archivo Python en busca de errores y advertencias."""
    codigo = leer_archivo(ruta)
    if codigo.startswith("ERROR"):
        return codigo
    errores = []
    advertencias = []
    try:
        ast.parse(codigo)
    except SyntaxError as e:
        errores.append(f"SyntaxError en línea {e.lineno}: {e.msg}")
    lineas = codigo.split("\n")
    for i, linea in enumerate(lineas, 1):
        if "except:" in linea and "except Exception" not in linea:
            advertencias.append(f"Línea {i}: except demasiado amplio")
        if len(linea) > 120:
            advertencias.append(f"Línea {i}: línea muy larga ({len(linea)} chars)")
        if "print(" in linea and "#" not in linea:
            advertencias.append(f"Línea {i}: print() encontrado (puede ser debug)")
    resumen = f"Archivo: {ruta}\n"
    resumen += f"Líneas: {len(lineas)}\n"
    resumen += f"Errores: {len(errores)}\n"
    resumen += f"Advertencias: {len(advertencias)}\n"
    if errores:
        resumen += "\nERRORES:\n" + "\n".join(errores)
    if advertencias:
        resumen += "\nADVERTENCIAS:\n" + "\n".join(advertencias)
    return resumen

def analizar_proyecto(carpeta: str) -> str:
    """Analiza un proyecto en busca de errores en los archivos Python."""
    if not os.path.exists(carpeta):
        return f"ERROR: Carpeta no encontrada: {carpeta}"
    reporte = []
    total_errores = 0
    total_archivos = 0
    for raiz, dirs, archivo
```

### autoeditor.py
```python
import os
import json
import shutil
import datetime
import ast

BASE = "C:/IA/AGENTE/MECANICO"
MECANICO_PY = "C:\\IA\\AGENTE\\MECANICO\\mecanico.py"

# ============================================
# MECANICO - Modulo Autoeditor con IA
# ============================================

def crear_directorio(ruta):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

def hacer_backup(archivo):
    ruta = os.path.join(BASE, archivo) if not os.path.isabs(archivo) else archivo
    if not os.path.isfile(ruta):
        return None
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = os.path.join(BASE, "memoria/backups", os.path.basename(ruta) + f".backup_{fecha}")
    crear_directorio(backup)
    shutil.copy2(ruta, backup)
    return f"Backup: {backup}"

def validar_python(codigo):
    try:
        ast.parse(codigo)
        return True, "Codigo valido"
    except SyntaxError as e:
        return False, f"Error de sintaxis linea {e.lineno}: {e.msg}"

def leer_archivo(archivo):
    ruta = os.path.join(BASE, archivo) if not os.path.isabs(archivo) else archivo
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception:
        return None

def escribir_archivo(archivo, contenido):
    ruta = os.path.join(BASE, archivo) if not os.path.isabs(archivo) else archivo
    crear_directorio(ruta)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    return f"OK Archivo guardado: {ruta}"

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

def agregar_trigger(trigger, nombre_modulo):
    """
```

### bucle_mejora.py
```python
import os

MAX_INTENTOS = 5
KEYWORDS = ["mejora hasta", "perfeccionar", "bucle mejora", "iterar"]

def esta_limpio(analisis_texto):
    t = analisis_texto.lower()
    señales_ok = ["no se encontraron errores", "no hay errores", "codigo limpio", "sin problemas", "no encontre bugs", "no se detectaron problemas"]
    if any(s in t for s in señales_ok):
        return True
    señales_mal = ["error", "bug", "problema", "falta", "deberia", "mejora posible", "duplicado"]
    cantidad_señales = sum(1 for s in señales_mal if s in t)
    return cantidad_señales == 0

def bucle_mejorar_archivo(ruta, preguntar_fn, modulos):
    if "analizador" not in modulos or "reparador" not in modulos:
        return "ERROR: faltan modulos analizador o reparador"
    if not os.path.exists(ruta):
        return f"ERROR: archivo no encontrado: {ruta}"

    log = []
    log.append(f"Iniciando bucle de mejora para: {ruta}")
    log.append(f"Maximo {MAX_INTENTOS} intentos\n")

    for intento in range(1, MAX_INTENTOS + 1):
        log.append(f"--- Intento {intento}/{MAX_INTENTOS} ---")
        log.append("Analizando con IA...")
        analisis = modulos["analizador"].ejecutar("analizar", f"analizar ia {ruta}")

        if esta_limpio(analisis):
            log.append("OK El archivo esta limpio, sin problemas detectados.")
            log.append(f"\nEXITO: se logro en {intento} intento(s)")
            return "\n".join(log)

        log.append(f"Se detectaron problemas:\n{analisis[:400]}\n")
        log.append("Aplicando mejora...")
        resultado_mejora = modulos["reparador"].ejecutar("mejorar", f"mejorar {ruta}")
        log.append(resultado_mejora[:300])
        log.append("")

        if "ERROR" in resultado_mejora and "Ninguna API" in resultado_mejora:
            log.append("ERROR: no se pudo generar una mejora valida, deteniendo bucle.")
            return "\n".join(log)

    log.append(f"\nLIMITE ALCANZADO: se hicieron {MAX_INTENTOS} intentos sin lograr version 100% limpia.")
    log.
```

### buscador_web.py
```python
import subprocess
import json

KEYWORDS = ["buscar web", "buscar internet", "buscar en internet", "investigar", "verificar"]

def ejecutar_comando(comando):
    import os
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=30, shell=True, encoding="utf-8", errors="ignore", env=env)
        return resultado.stdout.strip() if resultado.returncode == 0 else f"ERROR: {resultado.stderr.strip()}"
    except Exception as e:
        return f"ERROR: {e}"

def buscar(query, max_resultados=5):
    comando = f'zero-search "{query}" --json'
    salida = ejecutar_comando(comando)
    if salida.startswith("ERROR"):
        return salida
    try:
        data = json.loads(salida)
        sources = data.get("sources", [])
        texto = f"Resultados para '{query}':\n\n"
        for i, r in enumerate(sources[:max_resultados], 1):
            titulo = r.get("title", "Sin titulo")
            url = r.get("url", "")
            snippet = (r.get("snippet", ""))[:200]
            texto += f"{i}. {titulo}\n   {snippet}\n   {url}\n\n"
        if not sources:
            texto += "(sin fuentes encontradas)"
        return texto
    except Exception as e:
        return f"ERROR parseando: {e}\n{salida[:500]}"

def obtener_contexto(query):
    comando = f'zero-context "{query}"'
    return ejecutar_comando(comando)

def verificar(afirmacion):
    comando = f'zero-verify "{afirmacion}" --json'
    salida = ejecutar_comando(comando)
    if salida.startswith("ERROR"):
        return salida
    try:
        data = json.loads(salida)
        return json.dumps(data, indent=2, ensure_ascii=False)[:1500]
    except Exception:
        return salida[:1500]

def ejecutar(accion, texto):
    t = texto.lower()
    palabras = texto.split()
    if "verificar" in t:
        afirmacion = " ".join(palabras[1:])
        return verificar(afirmacion)
    elif "contexto" in t:
        query = " ".join(palabra
```

### explorador.py
```python
import os
import shutil
import datetime

KEYWORDS = ["explorar", "listar carpeta", "ver carpeta", "buscar archivo"]

def listar(ruta):
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    if not os.path.isdir(ruta):
        return f"ERROR: No es una carpeta: {ruta}"
    items = os.listdir(ruta)
    if not items:
        return f"Carpeta vacia: {ruta}"
    resultado = f"Contenido de {ruta}:\n"
    carpetas = []
    archivos = []
    for item in sorted(items):
        ruta_item = os.path.join(ruta, item)
        if os.path.isdir(ruta_item):
            carpetas.append(f"  [DIR] {item}")
        else:
            size = os.path.getsize(ruta_item)
            size_str = f"{size} bytes" if size < 1024 else f"{round(size/1024, 1)} KB"
            archivos.append(f"  [FILE] {item} ({size_str})")
    resultado += "\n".join(carpetas + archivos)
    resultado += f"\n\nTotal: {len(carpetas)} carpetas, {len(archivos)} archivos"
    return resultado

def buscar(ruta, patron):
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    encontrados = []
    for raiz, dirs, archivos in os.walk(ruta):
        dirs[:] = [d for d in dirs if d not in ["__pycache__", ".git", "node_modules"]]
        for archivo in archivos:
            if patron.lower() in archivo.lower():
                encontrados.append(os.path.join(raiz, archivo))
    if not encontrados:
        return f"No se encontro '{patron}' en {ruta}"
    return f"Encontrados {len(encontrados)} archivos:\n" + "\n".join(encontrados[:20])

def crear_carpeta(ruta):
    try:
        os.makedirs(ruta, exist_ok=True)
        return f"OK Carpeta creada: {ruta}"
    except Exception as e:
        return f"ERROR: {e}"

def copiar(origen, destino):
    try:
        if os.path.isdir(origen):
            shutil.copytree(origen, destino)
        else:
            shutil.copy2(origen, destino)
        return f"OK Copiado: {origen} -> {destino}"
    except Exception as e:
    
```

### generador.py
```python
import os
import ast
import importlib
BASE = "C:/IA/AGENTE/MECANICO"
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
def validar_python(codigo):
    try:
        ast.parse(codigo)
        return True, "OK"
    except SyntaxError as e:
        return False, f"SyntaxError linea {e.lineno}: {e.msg}"
def generar_modulo(descripcion, nombre, preguntar_fn):
    log = []
    log.append(f"Generando modulo: {nombre}")
    prompt = (
        "Sos un experto en Python. Crea un modulo Python completo segun esta descripcion.\n"
        "REGLAS CRITICAS:\n"
        "1. El modulo DEBE tener una funcion llamada ejecutar(accion, texto) al final.\n"
        "2. La funcion ejecutar interpreta el texto y llama a las funciones del modulo.\n"
        "3. El modulo debe tener una variable KEYWORDS con lista de palabras clave.\n"
        "4. Usa solo librerias de Python estandar o muy comunes (requests, os, json, etc).\n"
        "5. Maneja todos los errores con try/except.\n"
        "6. Responde SOLO con el codigo Python entre triple backticks.\n\n"
        f"Descripcion del modulo: {descripcion}\n\n"
        "Devolvé SOLO el codigo Python completo:"
    )
    from config import APIS
    apis_orden = ["groq", "gemini", "cerebras", "zai", "ollama"]
    apis_activas = [a for a in apis_orden if a in APIS and APIS[a]["activa"] and (APIS[a]["key"] or a == "ollama")]
    codigo_nuevo = None
    api_usada = None
    for api in apis_activas:
        try:
            respuesta = preguntar_fn(prompt, api=api)
            codigo = extraer_codigo(respuesta)
            if not codigo:
                continue
            valido, msg = validar_pytho
```

### git_manager.py
```python
import os
import subprocess
import datetime

BASE = "C:/IA/AGENTE/MECANICO"

def ejecutar_git(comando):
    try:
        resultado = subprocess.run(
            comando,
            cwd=BASE,
            capture_output=True,
            text=True,
            shell=True
        )
        if resultado.returncode == 0:
            return True, resultado.stdout.strip()
        else:
            return False, resultado.stderr.strip()
    except Exception as e:
        return False, str(e)

def commit_automatico(mensaje=None):
    if not mensaje:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"MECANICO auto-commit {fecha}"
    ok, out = ejecutar_git("git add .")
    if not ok:
        return f"ERROR en git add: {out}"
    ok, out = ejecutar_git(f'git commit -m "{mensaje}"')
    if not ok:
        if "nothing to commit" in out or "nothing added" in out:
            return "INFO: No hay cambios para commitear"
        return f"ERROR en git commit: {out}"
    return f"OK Commit: {mensaje}"

def push():
    ok, out = ejecutar_git("git push origin master")
    if not ok:
        return f"ERROR en git push: {out}"
    return f"OK Push exitoso"

def commit_y_push(mensaje=None):
    resultado_commit = commit_automatico(mensaje)
    if "ERROR" in resultado_commit:
        return resultado_commit
    resultado_push = push()
    return f"{resultado_commit}\n{resultado_push}"

def solo_push():
    return push()

def ver_estado():
    ok, out = ejecutar_git("git status")
    return out

def ver_historial(n=5):
    ok, out = ejecutar_git(f"git log --oneline -{n}")
    return out

def ejecutar(accion, texto):
    t = texto.lower()
    if "push" in t:
        resultado_commit = commit_automatico()
        if "ERROR" in resultado_commit:
            return solo_push()
        return f"{resultado_commit}\n{solo_push()}"
    elif "estado" in t or "status" in t:
        return ver_estado()
    elif "historial" in t or "log" in t:
        return ver_
```

### github_reader.py
```python
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
            return base64.b64decode(data["content"]).decode("utf-8", e
```

### github_scout.py
```python
import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
KEYWORDS = ["github", "scout", "buscar repos", "repositorios"]

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

KEYWORDS_RELEVANTES = [
    "repair", "fix", "analysis", "agent", "improvement",
    "refactor", "lint", "debug", "ast", "syntax", "code",
    "reparar", "analisis", "agente", "mejora", "codigo"
]

def es_relevante(repo):
    texto = f"{repo.get('name','')} {repo.get('description','')}".lower()
    return any(kw in texto for kw in KEYWORDS_RELEVANTES)

def buscar_repos(query, max_resultados=5):
    try:
        query_encoded = query.replace(" ", "+")
        url = f"https://api.github.com/search/repositories?q={query_encoded}&sort=stars&order=desc&per_page={max_resultados}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return f"ERROR: {r.status_code}"
        repos = r.json().get("items", [])
        if not repos:
            return f"No se encontraron repos para: {query}"
        resultado = f"Repos para '{query}':\n"
        for repo in repos:
            desc = (repo['description'] or 'Sin descripcion')[:80]
            resultado += f"  {repo['full_name']} ({repo['stargazers_count']} estrellas)\n"
            resultado += f"  {desc}\n  {repo['html_url']}\n\n"
        return resultado
    except Exception as e:
        return f"ERROR: {e}"

def traducir_resumir(desc, preguntar_fn):
    if not desc or desc == "Sin descripcion":
        return "Sin descripcion"
    prompt = f"Traducí y resumí en maximo 60 caracteres en español: {desc}"
    try:
        resultado = preguntar_fn(prompt, api="ollama")
        return resultado.strip()[:60]
    except Exception:
        return desc[:60]

def scout_para_mecanico(query_usuario, preguntar_fn):
    query = f"{query_usuario}+language:python"
    log = []
    l
```

### lector_contexto.py
```python
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
# internamente para llamar a esta nu
```

### memoria_historial.py
```python
import os
import logging
from datetime import datetime

# Configura el logging
logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Variable KEYWORDS con lista de palabras clave
KEYWORDS = ["registrar", "ver", "historial"]

# Constante global para la ruta del historial
HISTORIAL_PATH = "C:/IA/AGENTE/MECANICO/memoria/historial.log"

def registrar_evento(accion, detalle):
    """
    Registra un evento en el historial.log
    """
    try:
        # Crea el directorio si no existe
        os.makedirs(os.path.dirname(HISTORIAL_PATH), exist_ok=True)
        
        # Escribe la fecha, hora, accion y detalle en el archivo
        with open(HISTORIAL_PATH, "a", encoding='utf-8') as archivo:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"{fecha_hora} - {accion} - {detalle}\n")
    except Exception as e:
        logging.error(f"Error al registrar evento: {e}")

def ver_historial():
    """
    Lee las ultimas 20 lineas del historial.log
    """
    try:
        # Verifica si el archivo historial.log existe
        if os.path.exists(HISTORIAL_PATH):
            # Lee las ultimas 20 lineas del archivo
            with open(HISTORIAL_PATH, "r", encoding='utf-8') as archivo:
                lineas = archivo.readlines()
                ultimas_lineas = lineas[-20:]
                return "".join(ultimas_lineas)
        else:
            return "No hay historial registrado"
    except Exception as e:
        logging.error(f"Error al ver historial: {e}")

def ejecutar(accion, texto):
    try:
        t = texto.lower()
        if "registrar" in t:
            partes = texto.split("registrar", 1)
            detalle = partes[1].strip() if len(partes) > 1 else texto
            registrar_evento("registro", detalle)
            return f"Evento registrado: {detalle}"
        else:
            return ver_historial()
    except Exception as e:
        logging.error(f"Erro
```

### nvidia_selector.py
```python
import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

NVIDIA_KEY = os.getenv("NVIDIA_API_KEY")
KEYWORDS = ["nvidia", "nim", "modelos nvidia"]

BASE_URL = "https://integrate.api.nvidia.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NVIDIA_KEY}",
    "Content-Type": "application/json"
}

MODELOS_RECOMENDADOS = {
    "codigo":     "qwen/qwen2.5-coder-32b-instruct",
    "razonamiento": "deepseek-ai/deepseek-r1",
    "general":    "meta/llama-3.3-70b-instruct",
    "rapido":     "meta/llama-3.1-8b-instruct",
    "potente":    "minimax/minimax-m2.7"
}

def listar_modelos():
    try:
        r = requests.get(f"{BASE_URL}/models", headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return f"ERROR: {r.status_code}"
        modelos = r.json().get("data", [])
        resultado = f"MODELOS NVIDIA NIM DISPONIBLES ({len(modelos)} total):\n\n"
        for m in modelos[:20]:
            resultado += f"  {m['id']}\n"
        if len(modelos) > 20:
            resultado += f"  ... y {len(modelos)-20} mas\n"
        resultado += f"\nRECOMENDADOS PARA MECANICO:\n"
        for uso, modelo in MODELOS_RECOMENDADOS.items():
            resultado += f"  {uso}: {modelo}\n"
        return resultado
    except Exception as e:
        return f"ERROR: {e}"

def cambiar_modelo(nombre):
    try:
        from config import APIS
        import json
        config_path = "C:/IA/AGENTE/MECANICO/config.py"
        with open(config_path, "r", encoding="utf-8") as f:
            contenido = f.read()
        if '"nvidia"' not in contenido and "'nvidia'" not in contenido:
            return "ERROR: nvidia no esta en config.py"
        modelo_actual = APIS.get("nvidia", {}).get("modelo", "")
        contenido_nuevo = contenido.replace(
            f'"modelo": "{modelo_actual}"',
            f'"modelo": "{nombre}"',
            1
        )
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(contenido_nuevo)
  
```

### orquestador.py
```python
import json
import re

KEYWORDS = []

MODULOS_DISPONIBLES = {
    "analizar": "analizar <ruta_archivo.py> - analiza UN archivo Python. analizar proyecto <ruta_carpeta> - analiza TODOS los archivos de una carpeta (usar este para carpetas/proyectos). analizar ia <ruta_archivo.py> - analisis profundo con IA de un archivo",
    "reparar": "reparar <ruta> - corrige bugs y errores en un archivo",
    "mejorar": "mejorar <ruta> - aplica mejoras de calidad y arquitectura",
    "revertir": "revertir <archivo> - restaura el ultimo backup. revertir listar <archivo> para ver backups",
    "explorar": "explorar listar <ruta> / explorar buscar <patron> <ruta> / explorar leer <ruta> / explorar info <ruta>",
    "leer": "leer <ruta> y <pregunta> - lee un archivo y responde una pregunta sobre el con IA",
    "git": "git estado / git push / git historial - operaciones de control de versiones",
    "generar": "generar <descripcion> como <nombre> - crea un modulo nuevo desde cero",
    "github": "github leer <url> - analiza un repo de GitHub e implementa si es chico",
    "scout": "scout <tema> - busca repos de GitHub utiles",
    "tokens": "tokens / tokens historial / tokens limites - consumo de las APIs"
}

def intentar_modelos_nvidia(prompt, preguntar_fn):
    try:
        from config import NVIDIA_FALLBACK
    except ImportError:
        NVIDIA_FALLBACK = ["moonshotai/kimi-k2.6"]
    import os
    from dotenv import load_dotenv
    load_dotenv("C:/IA/AGENTE/MECANICO/.env")
    key = os.getenv("NVIDIA_API_KEY")
    import requests
    for modelo in NVIDIA_FALLBACK:
        try:
            headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
            body = {"model": modelo, "messages": [{"role": "user", "content": prompt}], "max_tokens": 2000, "stream": False}
            r = requests.post("https://integrate.api.nvidia.com/v1/chat/completions", headers=headers, json=body, timeout=60)
            data = r.json()
            contenido = data["choices"][
```

### reinicio.py
```python
import os
import sys
import subprocess

# Lista de palabras clave
KEYWORDS = ["reiniciar", "restart"]

def reiniciar():
    """
    Reinicia el proceso actual y vuelve a lanzar python mecanico.py
    """
    try:
        # Obtenemos el nombre del archivo actual
        archivo_actual = sys.argv[0]
        
        # Ejecutamos el comando para reiniciar el proceso
        subprocess.Popen([sys.executable, archivo_actual])
        
        # Matamos el proceso actual
        os._exit(0)
    except Exception as e:
        print(f"Error al reiniciar: {str(e)}")

def ejecutar(accion, texto):
    """
    Interpreta el texto y llama a las funciones del módulo
    """
    try:
        reiniciar()
        return "Reiniciando MECANICO..."
    except Exception as e:
        return f"Error al ejecutar la acción: {str(e)}"

# Llamamos a la función ejecutar
if __name__ == "__main__":
    # Simulamos una llamada a la función ejecutar
    ejecutar("reiniciar", "reiniciar el proceso")

```

### reparador.py
```python
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

    if not apis_activas:
        return None, None

    for api in apis_activas:
        try:
   
```

### revertir.py
```python
import os
import shutil
import glob
import re
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

def revertir(archivo: str, indice: int = 0) -> str:
    """
    Revierte un archivo a su versión más reciente.

    Args:
    archivo (str): Ruta del archivo.
    indice (int): Indice del backup a utilizar (0 para el más reciente).

    Returns:
    str: Mensaje de confirmación de la reversión.
    """
    if not archivo:
        raise ValueError("El archivo no puede ser vacío")

    if indice < 0:
        raise ValueError("El indice no puede ser negativo")

    nombre = os.path.basename(archivo)
    patron = os.path.join(BACKUPS, f"{nombre}.backup_*")
    backups = sorted(glob.glob(patron), reverse=True)
    if not backups:
        raise ValueError(f"No hay backups de {nombre}")

    if indice == 0 or indice > len(backups):
        indice = 0

    backup_seleccionado = backups[indice]
    ruta_destino = os.path.abspath(archivo)
    try:
        shutil.copy2(backup_seleccionado, ruta_destino)
        return f"OK Revertido a: {os.path.basename(backup_seleccionado)}\nArchivo restaurado: {ruta_destino}"
    except Exception as e:
        raise ValueError(f"Error al revertir el archivo: {e}")

def ejecutar(accion, texto):
    """
    Ejecuta una acción sobre un archivo.
    
    Parametros:
    accion (str): A
```

### tester.py
```python
import importlib.util
import inspect
import os
import traceback

KEYWORDS = ['mechanico', 'modulo']

def verificar_estructura(ruta_archivo):
    try:
        spec = importlib.util.spec_from_file_location('modulo', ruta_archivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        
        if not hasattr(modulo, 'KEYWORDS') or not isinstance(modulo.KEYWORDS, list):
            return False, "La variable KEYWORDS no existe o no es una lista"
        
        if not hasattr(modulo, 'ejecutar') or not inspect.isfunction(modulo.ejecutar):
            return False, "La función ejecutar no existe o no es una función"
        
        if len(inspect.signature(modulo.ejecutar).parameters) != 2:
            return False, "La función ejecutar no acepta 2 parámetros posicionales"
        
        return True, ""
    
    except Exception as e:
        return False, str(e)

def probar_ejecucion(ruta_archivo):
    try:
        spec = importlib.util.spec_from_file_location('modulo', ruta_archivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        
        try:
            resultado = modulo.ejecutar('prueba', 'texto de prueba')
            return True, str(resultado)
        except Exception as e:
            return False, str(e)
    
    except Exception as e:
        return False, str(e)

def ejecutar(accion, texto):
    palabras = texto.split()
    ruta_archivo = palabras[-1] if palabras else texto
    estructura_valida, mensaje_estructura = verificar_estructura(ruta_archivo)
    
    if not estructura_valida:
        return f"Error de estructura: {mensaje_estructura}"
    
    ejecucion_valida, mensaje_ejecucion = probar_ejecucion(ruta_archivo)
    
    if not ejecucion_valida:
        return f"Error de ejecución: {mensaje_ejecucion}"
    
    return f"Pasó la prueba de estructura y ejecución. Resultado: {mensaje_ejecucion}"

```

### texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial.py
```python
import os
import datetime
from os import path

# Lista de palabras clave
KEYWORDS = ["registrar", "evento", "ver", "historial"]

def registrar_evento(accion, detalle):
    """
    Registra un evento en el historial.
    
    :param accion: La accion realizada
    :param detalle: El detalle del evento
    """
    try:
        # Obtener la fecha y hora actuales
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Abrir el archivo de historial en modo append
        with open("historial.log", "a") as archivo:
            # Escribir la linea con la fecha y hora, accion y detalle
            archivo.write(f"{fecha_hora} - {accion}: {detalle}\n")
    except Exception as e:
        print(f"Error al registrar evento: {e}")

def ver_historial():
    """
    Lee las ultimas 20 lineas del historial.
    
    :return: Las ultimas 20 lineas del historial
    """
    try:
        # Verificar si el archivo de historial existe
        if not path.exists("historial.log"):
            return []
        
        # Abrir el archivo de historial en modo read
        with open("historial.log", "r") as archivo:
            # Leer todas las lineas del archivo
            lineas = archivo.readlines()
            
            # Devolver las ultimas 20 lineas
            return lineas[-20:]
    except Exception as e:
        print(f"Error al ver historial: {e}")

def ejecutar(accion, texto):
    """
    Interpreta el texto y llama a las funciones del modulo.
    
    :param accion: La accion a realizar
    :param texto: El texto a interpretar
    """
    try:
        # Interpretar el texto
        if accion == "registrar":
            # Registrar un evento
            detalle = texto
            registrar_evento(accion, detalle)
        elif accion == "ver":
            # Ver el historial
            historial = ver_historial()
            for linea in historial:
                print(linea.strip())
        else:
            print("Accion no reconocida
```

### token_monitor.py
```python
import os
import json
import datetime
from dotenv import load_dotenv

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

KEYWORDS = ["tokens", "uso", "monitor tokens", "consumo", "limite", "costo", "gasto"]
LOG_FILE = "C:/IA/AGENTE/MECANICO/memoria/token_log.json"

LIMITES = {
    "groq":     {"por_minuto": 12000,   "por_dia": 500000,  "precio_input": 0.59,  "precio_output": 0.79},
    "gemini":   {"por_minuto": 1000000, "por_dia": 1500000, "precio_input": 0.15,  "precio_output": 0.60},
    "cerebras": {"por_minuto": 60000,   "por_dia": 1000000, "precio_input": 0.60,  "precio_output": 1.00},
    "zai":      {"por_minuto": 10000,   "por_dia": 100000,  "precio_input": 0.10,  "precio_output": 0.30},
    "ollama":   {"por_minuto": -1,      "por_dia": -1,      "precio_input": 0.00,  "precio_output": 0.00}
}

def cargar_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_log(data):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def registrar_uso(api, tokens_input=0, tokens_output=0):
    log = cargar_log()
    ahora = datetime.datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%Y-%m-%d %H:00")
    if api not in log:
        log[api] = {"dias": {}, "horas": {}}
    if fecha not in log[api]["dias"]:
        log[api]["dias"][fecha] = {"input": 0, "output": 0}
    if hora not in log[api]["horas"]:
        log[api]["horas"][hora] = {"input": 0, "output": 0}
    log[api]["dias"][fecha]["input"] += tokens_input
    log[api]["dias"][fecha]["output"] += tokens_output
    log[api]["horas"][hora]["input"] += tokens_input
    log[api]["horas"][hora]["output"] += tokens_output
    guardar_log(log)

def calcular_costo(api, tokens_input, tokens_output):
    limites = LIMITES.get(api, {})
    precio_in = limites.get("precio_input", 0)
    preci
```

### uptime.py
```python
import logging
import platform
import psutil
import time
from typing import Optional

# Configuración de logging
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    datefmt=LOG_DATE_FORMAT
)

class Sistema:
    def __init__(self) -> None:
        self.boot_time: Optional[float] = None

    def obtener_boot_time(self) -> Optional[float]:
        """Obtiene el tiempo de arranque del sistema"""
        if self.boot_time is None:
            try:
                self.boot_time = psutil.boot_time()
            except psutil.Error as e:
                logging.error(f"Error al obtener el tiempo de arranque: {str(e)}")
        return self.boot_time

    def calcular_uptime(self) -> Optional[str]:
        """Calcula el tiempo de actividad del sistema"""
        boot_time = self.obtener_boot_time()
        if boot_time is not None:
            uptime = time.time() - boot_time
            horas = int(uptime // 3600)
            minutos = int((uptime % 3600) // 60)
            segundos = int(uptime % 60)
            return f"{horas} horas, {minutos} minutos y {segundos} segundos"
        else:
            return None

    def ejecutar(self, texto: str) -> None:
        """Interpreta el texto y llama a las funciones del módulo"""
        if any(palabra in texto.lower() for palabra in ["uptime", "tiempo", "corriendo"]):
            try:
                uptime = self.calcular_uptime()
                if uptime is not None:
                    logging.info(f"El sistema lleva {uptime} en ejecución")
            except Exception as e:
                logging.error(f"Error al ejecutar la acción: {str(e)}")
        else:
            logging.info("Acción no reconocida")

def main() -> None:
    sistema = Sistema()
    texto = "¿Cuánto tiempo lleva el sistema en ejecución?"
    sistema.ejecutar(texto)

if __name__ == "__main__":
    main()
```

## CONFIG
```python
# ============================================
# MECANICO IA - Configuracion central
# ============================================
import os
from dotenv import load_dotenv

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

RUTAS = {
    "workspace":  "C:/IA/AGENTE/MECANICO/workspace",
    "proyectos":  "C:/IA/AGENTE/MECANICO/proyectos",
    "sesiones":   "C:/IA/AGENTE/MECANICO/memoria/sesiones",
    "errores":    "C:/IA/AGENTE/MECANICO/memoria/errores",
    "backups":    "C:/IA/AGENTE/MECANICO/memoria/backups",
    "modulos":    "C:/IA/AGENTE/MECANICO/modulos",
}

APIS = {
    "groq":     {"key": os.getenv("GROQ_API_KEY"),     "activa": True,  "modelo": "llama-3.3-70b-versatile"},
    "gemini":   {"key": os.getenv("GEMINI_API_KEY"),   "activa": True,  "modelo": "gemini-2.5-flash"},
    "cerebras": {"key": os.getenv("CEREBRAS_API_KEY"), "activa": True,  "modelo": "gpt-oss-120b"},
    "nvidia":   {"key": os.getenv("NVIDIA_API_KEY"), "activa": True, "modelo": "moonshotai/kimi-k2.6"},
    "zai":      {"key": os.getenv("ZAI_API_KEY"),      "activa": True,  "modelo": "glm-4.7-flash"},
    "ollama":   {"key": None,                           "activa": True,  "modelo": "gemma3:4b", "url": "http://localhost:11434"},
}

MODOS = {
    "auto":   "MECANICO trabaja solo sin pedir confirmacion",
    "manual": "MECANICO pide confirmacion antes de cada accion",
    "mixto":  "MECANICO decide segun la complejidad",
}

MODO_ACTUAL = "manual"
GITHUB_REPO = os.getenv("GITHUB_REPO")
BASE = "C:/IA/AGENTE/MECANICO"

NVIDIA_FALLBACK = [
    "moonshotai/kimi-k2.6",
    "mistralai/mistral-large-3-675b-instruct-2512",
    "nvidia/nemotron-3-super-120b-a12b",
    "deepseek-ai/deepseek-v4-pro",
    "meta/llama-3.3-70b-instruct",
]

```

## MECANICO.PY - TRIGGERS ACTIVOS
- if archivo.endswith(".py") and not archivo.startswith("_"):
- if archivo.endswith(".py") and not archivo.startswith("_"):
- if entrada.lower().startswith("ejecutar json"):
- if entrada.lower().startswith("generar"):
- if entrada.lower().startswith("nvidia"):
- if entrada.lower().startswith("github"):
- if entrada.lower().startswith("scout"):
- if entrada.lower().startswith("tokens"):
- if entrada.lower().startswith("mejorar"):
- if entrada.lower().startswith("reparar"):
- if entrada.lower().startswith("revertir"):
- if entrada.lower().startswith("analizar"):
- if entrada.lower().startswith("leer"):
- if entrada.lower().startswith("explorar"):
- if entrada.lower().startswith("git"):
- if entrada.lower().startswith("buscar"):
- if entrada.lower().startswith("bucle"):
- if entrada.lower().startswith("reinicio"):
- if entrada.lower().startswith("uptime"):
- if entrada.lower().startswith("tester"):
- if entrada.lower().startswith("texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial"):
- if entrada.lower().startswith("memoria_historial"):

## APIS CONFIGURADAS
- groq: llama-3.3-70b-versatile
- gemini: gemini-2.5-flash
- cerebras: gpt-oss-120b
- nvidia: moonshotai/kimi-k2.6 (fallback: mistral-large, nemotron, deepseek-v4, llama-3.3)
- zai: glm-4.7-flash
- ollama: gemma3:4b (local)

## PENDIENTES PROXIMA SESION
- Arreglar orquestador (devuelve None en pedidos complejos)
- Implementar Headoom MCP
- Implementar CodeBase Memory MCP
- Auto-reparacion y auto-mejora de MECANICO
- Estabilizar modo Auto (orquestador)