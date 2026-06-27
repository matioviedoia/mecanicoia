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

TEMAS = [
    "code repair agent",
    "auto fix code AI",
    "code analysis agent",
    "python code improvement",
    "static analysis tool"
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

def scout_para_mecanico(preguntar_fn):
    log = []
    log.append("Buscando repos para MECANICO...\n")
    todos_repos = []
    for tema in TEMAS:
        try:
            query_encoded = tema.replace(" ", "+")
            url = f"https://api.github.com/search/repositories?q={query_encoded}&sort=stars&order=desc&per_page=5"
            r = requests.get(url, headers=HEADERS, timeout=10)
            if r.status_code == 200:
                for repo in r.json().get("items", []):
                    if repo["full_name"] not in [x["full_name"] for x in todos_repos]:
                        todos_repos.append(repo)
        except Exception:
            continue
    # Pre-filtro por relevancia
    filtrados = [r for r in todos_repos if es_relevante(r)]
    filtrados.sort(key=lambda x: x["stargazers_count"], reverse=True)
    top = filtrados[:5]
    if not top:
        return "No se encontraron repos relevantes"
    log.append(f"Encontrados {len(todos_repos)} repos, {len(filtrados)} relevantes, analizando top 5...\n")
    # Traducir y resumir con Ollama (barato)
    resumen_compacto = "REPOS PARA MECANICO:\n\n"
    for i, repo in enumerate(top, 1):
        desc_original = repo.get('description') or 'Sin descripcion'
        desc_es = traducir_resumir(desc_original, preguntar_fn)
        resumen_compacto += f"{i}. {repo['full_name']} ({repo['stargazers_count']} estrellas)\n"
        resumen_compacto += f"   {desc_es}\n"
        resumen_compacto += f"   {repo['html_url']}\n\n"
    log.append(resumen_compacto)
    # Analisis final con Gemini (1 sola llamada, texto corto)
    prompt = (
        "Sos experto en agentes IA Python.\n"
        "Para cada repo indica en 1 linea que funcionalidad util podria integrarse en MECANICO,\n"
        "un agente que analiza y repara codigo Python.\n"
        "Maximo 150 palabras total. Responde en español.\n\n"
        + resumen_compacto
    )
    log.append("Analizando con Gemini...\n")
    analisis = None
    for api in ["gemini", "cerebras", "ollama"]:
        try:
            resultado = preguntar_fn(prompt, api=api)
            if resultado and "ERROR" not in resultado:
                analisis = f"[{api}]: {resultado}"
                break
        except Exception:
            continue
    log.append(analisis or "No se pudo analizar")
    return "\n".join(log)

def ejecutar(accion, texto):
    t = texto.lower()
    if "scout" in t or "mecanico" in t or "sugerir" in t:
        from mecanico import preguntar
        return scout_para_mecanico(preguntar)
    else:
        palabras = texto.split()
        query = " ".join(palabras[1:]) if len(palabras) > 1 else "code repair"
        return buscar_repos(query)
