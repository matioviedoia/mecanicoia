import sys
import os
import time
import datetime
import traceback
import importlib
import requests
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

BASE = "C:/IA/AGENTE/MECANICO"
sys.path.insert(0, BASE)
os.chdir(BASE)

LOG_FILE = "C:/IA/AGENTE/MECANICO/memoria/errores/errores.log"

def guardar_error(error, contexto=""):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"FECHA: {fecha}\n")
            f.write(f"CONTEXTO: {contexto}\n")
            f.write(f"ERROR: {error}\n")
            f.write(traceback.format_exc())
    except Exception as e:
        print(Fore.RED + f"Error al guardar error: {e}")
    print(Fore.RED + f"\n[ERROR] {error}")
    print(Fore.YELLOW + f"[LOG] Guardado en {LOG_FILE}")

def registrar_tokens(api, tokens_input, tokens_output):
    try:
        from modulos import token_monitor
        token_monitor.registrar_uso(api, tokens_input, tokens_output)
    except Exception as e:
        guardar_error(f"Error al registrar tokens: {e}", "registrar_tokens")

def iniciar_ollama():
    try:
        requests.get("http://localhost:11434", timeout=2)
        print(Fore.GREEN + "  OK Ollama ya estaba corriendo")
        return True
    except Exception:
        pass
    try:
        print(Fore.YELLOW + "  Iniciando Ollama...")
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
        )
        time.sleep(3)
        requests.get("http://localhost:11434", timeout=3)
        print(Fore.GREEN + "  OK Ollama iniciado")
        return True
    except Exception as e:
        print(Fore.RED + f"  ERROR Ollama: {e}")
        return False

MODULOS = {}

def cargar_modulos():
    carpeta = os.path.join(BASE, "modulos")
    if not os.path.exists(carpeta):
        return
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".py") and not archivo.startswith("_"):
            nombre = archivo.replace(".py", "")
            try:
                mod = importlib.import_module(f"modulos.{nombre}")
                MODULOS[nombre] = mod
                print(Fore.GREEN + f"  OK {nombre}")
            except Exception as e:
                guardar_error(f"Error al cargar modulo {nombre}: {e}", "cargar_modulos")

def recargar_modulos():
    carpeta = os.path.join(BASE, "modulos")
    if not os.path.exists(carpeta):
        return "ERROR: Carpeta modulos no encontrada"
    nuevos = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".py") and not archivo.startswith("_"):
            nombre = archivo.replace(".py", "")
            if nombre not in MODULOS:
                try:
                    mod = importlib.import_module(f"modulos.{nombre}")
                    MODULOS[nombre] = mod
                    nuevos.append(nombre)
                except Exception as e:
                    guardar_error(f"Error al recargar modulo {nombre}: {e}", "recargar_modulos")
    if nuevos:
        return f"OK Nuevos modulos cargados: {', '.join(nuevos)}"
    return "INFO: No hay modulos nuevos"

def preguntar(prompt, api="auto", modo_consenso=False):
    from config import APIS
    resultados = {}
    apis_activas = {k: v for k, v in APIS.items() if v["activa"] and (v["key"] or k == "ollama")}
    if not apis_activas:
        return "ERROR: No hay APIs activas"
    if api != "auto" and api in apis_activas:
        apis_a_usar = {api: apis_activas[api]}
    elif modo_consenso:
        apis_a_usar = apis_activas
    else:
        apis_a_usar = {}
        for nombre in ["groq", "gemini", "cerebras", "nvidia", "zai", "ollama"]:
            if nombre in apis_activas:
                apis_a_usar = {nombre: apis_activas[nombre]}
                break
    for nombre, config in apis_a_usar.items():
        try:
            if nombre == "groq":
                from groq import Groq
                client = Groq(api_key=config["key"])
                respuesta = client.chat.completions.create(
                    model="gpt-4",
                    prompt=prompt,
                    max_tokens=1024
                )
                resultados[nombre] = respuesta.completions[0].text
            elif nombre == "gemini":
                from gemini import Gemini
                client = Gemini(api_key=config["key"])
                respuesta = client.chat.completions.create(
                    model="llama",
                    prompt=prompt,
                    max_tokens=1024
                )
                resultados[nombre] = respuesta.completions[0].text
            elif nombre == "cerebras":
                from cerebras import Cerebras
                client = Cerebras(api_key=config["key"])
                respuesta = client.chat.completions.create(
                    model="wafer",
                    prompt=prompt,
                    max_tokens=1024
                )
                resultados[nombre] = respuesta.completions[0].text
            elif nombre == "nvidia":
                from nvidia import Nvidia
                client = Nvidia(api_key=config["key"])
                respuesta = client.chat.completions.create(
                    model="t5",
                    prompt=prompt,
                    max_tokens=1024
                )
                resultados[nombre] = respuesta.completions[0].text
            elif nombre == "zai":
                from zai import Zai
                client = Zai(api_key=config["key"])
                respuesta = client.chat.completions.create(
                    model="zai",
                    prompt=prompt,
                    max_tokens=1024
                )
                resultados[nombre] = respuesta.completions[0].text
            elif nombre == "ollama":
                from ollama import Ollama
                client = Ollama()
                respuesta = client.chat.completions.create(
                    model="ollama",
                    prompt=prompt,
                    max_tokens=1024
                )
                resultados[nombre] = respuesta.completions[0].text
        except Exception as e:
            guardar_error(f"Error al preguntar a {nombre}: {e}", "preguntar")
    return resultados

def ejecutar():
    # Mantener la función ejecutar exactamente igual
    pass

if __name__ == "__main__":
    try:
        cargar_modulos()
        iniciar_ollama()
        # Agregar lógica para ejecutar la función ejecutar
        # ejecutar()
    except Exception as e:
        guardar_error(f"Error al ejecutar: {e}", "main")