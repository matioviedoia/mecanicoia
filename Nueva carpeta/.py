cat > /mnt/user-data/outputs/mecanico.py << 'ENDOFFILE'
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
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"FECHA: {fecha}\n")
            f.write(f"CONTEXTO: {contexto}\n")
            f.write(f"ERROR: {error}\n")
            f.write(traceback.format_exc())
    except Exception:
        pass
    print(Fore.RED + f"\n[ERROR] {error}")
    print(Fore.YELLOW + f"[LOG] Guardado en {LOG_FILE}")

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
        os.makedirs(carpeta, exist_ok=True)
        print(Fore.YELLOW + f"  Carpeta modulos creada en {carpeta}")
        return
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".py") and not archivo.startswith("_"):
            nombre = archivo.replace(".py", "")
            try:
                if nombre in MODULOS:
                    importlib.reload(MODULOS[nombre])
                else:
                    mod = importlib.import_module(f"modulos.{nombre}")
                    MODULOS[nombre] = mod
                print(Fore.GREEN + f"  OK {nombre}")
            except Exception as e:
                print(Fore.RED + f"  ERROR {nombre}: {e}")

def preguntar(prompt, api="auto", modo_consenso=False):
    try:
        from config import APIS
    except ImportError:
        print(Fore.RED + "ERROR: No se encuentra config.py")
        return "ERROR: Archivo config.py no encontrado"
    
    resultados = {}
    apis_activas = {k: v for k, v in APIS.items() if v.get("activa", False) and (v.get("key") or k == "ollama")}
    
    if not apis_activas:
        return "ERROR: No hay APIs activas"
    
    if api != "auto" and api in apis_activas:
        apis_a_usar = {api: apis_activas[api]}
    elif modo_consenso:
        apis_a_usar = apis_activas
    else:
        apis_a_usar = {}
        for nombre in ["groq", "gemini", "cerebras", "zai", "ollama"]:
            if nombre in apis_activas:
                apis_a_usar = {nombre: apis_activas[nombre]}
                break
    
    for nombre, config in apis_a_usar.items():
        try:
            if nombre == "groq":
                from groq import Groq
                client = Groq(api_key=config["key"])
                respuesta = client.chat.completions.create(
                    model=config["modelo"],
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=2000
                )
                resultados[nombre] = respuesta.choices[0].message.content
                
            elif nombre == "gemini":
                from google import genai
                client = genai.Client(api_key=config["key"])
                respuesta = client.models.generate_content(model=config["modelo"], contents=prompt)
                resultados[nombre] = respuesta.text
                
            elif nombre == "cerebras":
                from cerebras.cloud.sdk import Cerebras
                client = Cerebras(api_key=config["key"])
                respuesta = client.chat.completions.create(
                    model=config["modelo"],
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=2000
                )
                resultados[nombre] = respuesta.choices[0].message.content
                
            elif nombre == "zai":
                headers = {"Authorization": config["key"], "Content-Type": "application/json"}
                body = {"model": config["modelo"], "messages": [{"role": "user", "content": prompt}], "max_tokens": 2000}
                r = requests.post("https://open.bigmodel.cn/api/paas/v4/chat/completions", headers=headers, json=body, timeout=30)
                resultados[nombre] = r.json()["choices"][0]["message"]["content"]
                
            elif nombre == "ollama":
                import ollama as ol
                respuesta = ol.chat(model=config["modelo"], messages=[{"role": "user", "content": prompt}])
                resultados[nombre] = respuesta["message"]["content"]
                
        except Exception as e:
            guardar_error(str(e), f"API: {nombre}")
            resultados[nombre] = f"ERROR: {e}"
    
    if not resultados:
        return "ERROR: Todas las APIs fallaron"
    
    if modo_consenso:
        return resultados
    return list(resultados.values())[0]

def mostrar_menu_principal():
    print()
    print(Fore.CYAN + "=" * 55)
    print(Fore.CYAN + "   MECANICO IA - Agente Reparador v2.0")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "  1. Modo Manual    - vos le decis que hacer")
    print(Fore.WHITE + "  2. Modo Auto      - MECANICO trabaja solo")
    print(Fore.WHITE + "  3. Modo Consenso  - todas las APIs juntas")
    print(Fore.WHITE + "  4. Ver APIs       - estado de las APIs")
    print(Fore.WHITE + "  5. Cambiar API    - elegir con que IA trabajar")
    print(Fore.WHITE + "  6. Recargar módulos - recargar módulos sin reiniciar")
    print(Fore.WHITE + "  s. Salir")
    print(Fore.CYAN + "=" * 55)

def mostrar_menu_apis():
    try:
        from config import APIS
    except ImportError:
        print(Fore.RED + "ERROR: config.py no encontrado")
        return []
    
    print()
    print(Fore.CYAN + "=" * 55)
    print(Fore.CYAN + "   Elegir API activa")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "  0. Auto (groq > gemini > cerebras > zai > ollama)")
    apis = list(APIS.items())
    for i, (nombre, config) in enumerate(apis, 1):
        tiene_key = bool(config.get("key")) or nombre == "ollama"
        estado = Fore.GREEN + "OK" if (config.get("activa", False) and tiene_key) else Fore.RED + "OFF"
        modelo = config.get("modelo", "sin modelo")
        print(f"  {i}. {estado} {nombre:<12} {modelo}")
    print(Fore.CYAN + "=" * 55)
    return apis

def elegir_api():
    apis = mostrar_menu_apis()
    if not apis:
        return "auto"
    opcion = input(Fore.YELLOW + "Elegi 0 para auto o 1-" + str(len(apis)) + ": ").strip()
    if opcion == "0":
        print(Fore.GREEN + "\nAPI: Auto")
        return "auto"
    try:
        idx = int(opcion) - 1
        if 0 <= idx < len(apis):
            nombre = apis[idx][0]
            print(Fore.GREEN + f"\nAPI seleccionada: {nombre}")
            return nombre
    except Exception:
        pass
    print(Fore.RED + "Opcion invalida, usando auto")
    return "auto"

def ver_apis():
    try:
        from config import APIS
    except ImportError:
        print(Fore.RED + "ERROR: config.py no encontrado")
        return
    
    print()
    print(Fore.CYAN + "Estado de APIs:")
    for nombre, config in APIS.items():
        tiene_key = bool(config.get("key")) or nombre == "ollama"
        estado = Fore.GREEN + "OK" if (config.get("activa", False) and tiene_key) else Fore.RED + "INACTIVA"
        modelo = config.get("modelo", "sin modelo")
        print(f"  {estado} {nombre:<12} modelo: {modelo}")
    print()

def hacer_prompt(entrada, api_actual):
    return (
        "Sos MECANICO, un agente IA especializado en analizar, reparar y mejorar codigo.\n"
        "Siempre respondes en espanol. Sos directo y tecnico.\n"
        f"Fecha actual: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
        f"Usuario: {entrada}"
    )

def ejecutar_comando_modulo(comando, entrada):
    """Ejecuta un comando en un módulo específico"""
    comandos = {
        "ejecutar json": "autoeditor",
        "mejorar": "reparador",
        "reparar": "reparador",
        "revertir": "revertir",
        "analizar": "analizador",
        "leer": "lector_contexto",
        "explorar": "explorador",
        "git": "git_manager"
    }
    
    for cmd, modulo in comandos.items():
        if entrada.lower().startswith(cmd):
            if modulo in MODULOS:
                try:
                    resultado = MODULOS[modulo].ejecutar(cmd, entrada)
                    print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    return True
                except Exception as e:
                    guardar_error(str(e), f"Módulo {modulo}")
                    print(Fore.RED + f"\nError en módulo {modulo}: {e}")
                    return True
            else:
                print(Fore.YELLOW + f"\nMódulo {modulo} no cargado")
                return True
    return False

print()
print(Fore.CYAN + "=" * 55)
print(Fore.CYAN + "   MECANICO IA arrancando...")
print(Fore.CYAN + "=" * 55)

# Crear estructura de directorios
for dir_name in ["memoria/errores", "modulos", "backups", "temp"]:
    os.makedirs(os.path.join(BASE, dir_name), exist_ok=True)

print(Fore.WHITE + "\nVerificando Ollama:")
iniciar_ollama()

print(Fore.WHITE + "\nCargando modulos:\n")
cargar_modulos()

historial = []
modo_actual = "manual"
api_actual = "auto"

while True:
    try:
        mostrar_menu_principal()
        print(Fore.YELLOW + f"  [API activa: {api_actual}]")
        opcion = input(Fore.YELLOW + "Elegi 1, 2, 3, 4, 5, 6 o s: ").strip().lower()

        if opcion == "s":
            print(Fore.CYAN + "Hasta luego.")
            break

        elif opcion == "6":
            print(Fore.WHITE + "\nRecargando módulos...")
            cargar_modulos()
            print(Fore.GREEN + "Módulos recargados")

        elif opcion == "5":
            api_actual = elegir_api()

        elif opcion == "4":
            ver_apis()

        elif opcion == "3":
            print(Fore.GREEN + "\nModo Consenso activado.")
            try:
                entrada = input(Fore.YELLOW + "\nPregunta para todas las APIs: ").strip()
            except KeyboardInterrupt:
                continue
            if entrada:
                try:
                    print(Fore.WHITE + "Consultando todas las APIs...\n")
                    resultados = preguntar(hacer_prompt(entrada, "consenso"), modo_consenso=True)
                    if isinstance(resultados, dict):
                        for api, resp in resultados.items():
                            print(Fore.CYAN + f"\n[{api.upper()}]:")
                            print(Fore.WHITE + resp)
                    else:
                        print(Fore.RED + f"Error: {resultados}")
                except Exception as e:
                    guardar_error(str(e), "Modo consenso")
                    print(Fore.RED + f"Error en modo consenso: {e}")

        elif opcion == "2":
            print(Fore.GREEN + "\nModo Auto activado.")
            print(Fore.YELLOW + "MECANICO analizará y ejecutará tareas automáticamente...")
            try:
                entrada = input(Fore.YELLOW + "\nDescribí la tarea a realizar: ").strip()
                if entrada:
                    # Aquí iría la lógica de modo auto
                    print(Fore.WHITE + "\nAnalizando tarea...")
                    response = preguntar(
                        f"Sos MECANICO en modo auto. El usuario solicita: {entrada}\n"
                        "Analizá la solicitud y proponé un plan de acción detallado.",
                        api=api_actual
                    )
                    print(Fore.GREEN + f"\nMECANICO: {response}")
            except KeyboardInterrupt:
                continue

        elif opcion == "1":
            print(Fore.GREEN + f"\nModo Manual activado. API: {api_actual}")
            print(Fore.WHITE + "Comandos: 'api' cambiar API | 'apis' ver estado | 'menu' volver | 'salir' terminar")
            print(Fore.WHITE + "Comandos especiales: reparar, mejorar, analizar, git, leer, explorar")
            print(Fore.CYAN + "-" * 55)

            while True:
                try:
                    entrada = input(Fore.YELLOW + f"\n[{api_actual}] Vos: ").strip()
                except KeyboardInterrupt:
                    break

                if not entrada:
                    continue
                if entrada.lower() == "menu":
                    break
                if entrada.lower() == "salir":
                    sys.exit(0)
                if entrada.lower() == "apis":
                    ver_apis()
                    continue
                if entrada.lower() == "api":
                    api_actual = elegir_api()
                    continue

                # Verificar comandos de módulos
                if ejecutar_comando_modulo(entrada, entrada):
                    continue

                # Consulta normal a la API
                try:
                    print(Fore.WHITE + "Pensando...", end="", flush=True)
                    inicio = time.time()
                    respuesta = preguntar(hacer_prompt(entrada, api_actual), api=api_actual)
                    fin = round(time.time() - inicio, 2)
                    
                    if respuesta.startswith("ERROR:"):
                        print(Fore.RED + f"\rMECANICO [{api_actual}] ({fin}s): " + Fore.WHITE + respuesta)
                    else:
                        print(Fore.GREEN + f"\rMECANICO [{api_actual}] ({fin}s): " + Fore.WHITE + respuesta)
                        
                    # Guardar en historial
                    historial.append({
                        "fecha": datetime.datetime.now().isoformat(),
                        "api": api_actual,
                        "usuario": entrada,
                        "respuesta": respuesta
                    })
                    
                except Exception as e:
                    guardar_error(str(e), "Modo manual")
                    print(Fore.RED + f"\nError: {e}")

        else:
            print(Fore.YELLOW + "Opción no válida. Intentá de nuevo.")

    except KeyboardInterrupt:
        print(Fore.CYAN + "\nHasta luego.")
        break
    except Exception as e:
        guardar_error(str(e), "Loop principal")
        print(Fore.RED + "\nError capturado. MECANICO sigue funcionando.")
        continue
ENDOFFILE
echo "✅ mecanico.py creado exitosamente"
