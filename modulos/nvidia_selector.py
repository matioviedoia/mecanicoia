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
        return f"OK Modelo NVIDIA cambiado a: {nombre}\nReinicia MECANICO para aplicar el cambio."
    except Exception as e:
        return f"ERROR: {e}"

def ejecutar(accion, texto):
    t = texto.lower()
    if "listar" in t or "modelos" in t or "lista" in t:
        return listar_modelos()
    elif "cambiar" in t or "usar" in t:
        palabras = texto.split()
        modelo = palabras[-1] if len(palabras) > 1 else ""
        if not modelo:
            return "ERROR: Especifica el modelo. Ej: nvidia usar meta/llama-3.3-70b-instruct"
        return cambiar_modelo(modelo)
    else:
        return listar_modelos()
