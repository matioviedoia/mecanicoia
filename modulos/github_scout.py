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
    log.append(f"Buscando repos para '{query_usuario}'...\n")
    url = f'https://api.github.com/search/repositories?q={query.replace(chr(32),chr(43))}+language:python&sort=stars&order=desc&per_page=10'
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            log.append(f"ERROR: {r.status_code}")
            return "\n".join(log)
        repos = r.json().get('items', [])
        top = [repo for repo in repos if es_relevante(repo)]
        top.sort(key=lambda x: x["stargazers_count"], reverse=True)
        top = top[:5]
        log.append(f"Encontrados {len(top)} repos relevantes\n")
        resumen_compacto = f"REPOS:\n\n"
        for i, repo in enumerate(top, 1):
            desc_es = traducir_resumir(repo.get('description', ''), preguntar_fn)
            resumen_compacto += f"{i}. {repo['full_name']} ({repo['stargazers_count']} estrellas)\n"
            resumen_compacto += f"   {desc_es}\n"
            resumen_compacto += f"   {repo['html_url']}\n\n"
        log.append(resumen_compacto)
        prompt = (
            f"Sos experto en agentes IA Python.\n"
            "Para cada repo indica en 1 linea que funcionalidad especifica podria integrarse en MECANICO,\n"
            "un agente que analiza y repara codigo Python. Maximo 150 palabras. Responde en español.\n\n"
            + resumen_compacto[:1500]
        )
        log.append("Analizando con Gemini...\n")
        analisis = None
        for api in ["gemini", "cerebras", "ollama"]:
            try:
                resultado = preguntar_fn(prompt, api=api)
                if resultado and "ERROR" not in resultado:
                    analisis = f"[{api}]:\n{resultado}"
                    break
            except Exception:
                continue
        log.append(analisis or "No se pudo analizar")
        return "\n".join(log)
    except Exception as e:
        log.append(f"ERROR: {e}")
        return "\n".join(log)

def ejecutar(accion, texto):
    t = texto.lower()
    from mecanico import preguntar
    if "scout" in t or "mecanico" in t or "sugerir" in t:
        query = texto.replace("scout", "").strip()
        return scout_para_mecanico(query, preguntar)
    else:
        palabras = texto.split()
        query = " ".join(palabras[1:]) if len(palabras) > 1 else "code repair"
        return buscar_repos(query)