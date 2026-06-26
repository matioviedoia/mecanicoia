import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
KEYWORDS = ["github", "buscar proyectos", "scout", "repositorios", "repos"]

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

TEMAS_MECANICO = [
    "code repair agent python",
    "code analysis ai python",
    "auto fix code python",
    "ai code reviewer python",
    "static code analysis python",
    "code improvement agent"
]

def buscar_repos(query, max_resultados=5):
    try:
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={max_resultados}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return f"ERROR: {r.status_code} - {r.json().get('message', '')}"
        data = r.json()
        repos = data.get("items", [])
        if not repos:
            return f"No se encontraron repos para: {query}"
        resultado = f"Repos para '{query}':\n"
        for repo in repos:
            resultado += f"\n  {repo['full_name']} ({repo['stargazers_count']} estrellas)\n"
            resultado += f"  {repo['description'] or 'Sin descripcion'}\n"
            resultado += f"  {repo['html_url']}\n"
        return resultado
    except Exception as e:
        return f"ERROR: {e}"

def scout_para_mecanico(preguntar_fn):
    log = []
    log.append("Buscando proyectos utiles para MECANICO en GitHub...\n")
    todos_repos = []
    for tema in TEMAS_MECANICO:
        try:
            url = f"https://api.github.com/search/repositories?q={tema}&sort=stars&order=desc&per_page=3"
            r = requests.get(url, headers=HEADERS, timeout=10)
            if r.status_code == 200:
                repos = r.json().get("items", [])
                for repo in repos:
                    if repo["full_name"] not in [x["full_name"] for x in todos_repos]:
                        todos_repos.append(repo)
        except Exception:
            continue
    todos_repos.sort(key=lambda x: x["stargazers_count"], reverse=True)
    top_repos = todos_repos[:10]
    if not top_repos:
        return "No se encontraron repositorios"
    resumen = "TOP 10 REPOS PARA MECANICO:\n\n"
    for i, repo in enumerate(top_repos, 1):
        resumen += f"{i}. {repo['full_name']} ({repo['stargazers_count']} estrellas)\n"
        resumen += f"   {repo['description'] or 'Sin descripcion'}\n"
        resumen += f"   {repo['html_url']}\n\n"
    log.append(resumen)
    prompt = (
        "Sos un experto en desarrollo de agentes IA.\n"
        "Analizá estos repositorios de GitHub y decime cuales son mas utiles\n"
        "para mejorar MECANICO, un agente que analiza, repara y mejora codigo Python.\n"
        "Para cada repo util, sugeri especificamente que funcionalidad o tecnica se podria integrar.\n\n"
        f"{resumen}\n"
        "Respondé en español, sé conciso y específico."
    )
    log.append("Analizando con IA...\n")
    analisis = preguntar_fn(prompt)
    log.append(analisis)
    return "\n".join(log)

def ejecutar(accion, texto):
    t = texto.lower()
    if "scout" in t or "mecanico" in t or "sugerir" in t or "sugerencias" in t:
        from mecanico import preguntar
        return scout_para_mecanico(preguntar)
    else:
        palabras = texto.split()
        query = " ".join(palabras[1:]) if len(palabras) > 1 else "code repair python"
        return buscar_repos(query)
