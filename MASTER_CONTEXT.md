# 🧠 MASTER CONTEXT - MECANICO
Generado automáticamente el: 2026-07-09 23:15

Este archivo consolida la estructura, los archivos fuente principales y la lógica del proyecto para que cualquier IA pueda entender su contexto global inmediatamente y proponer modificaciones, depuraciones o extensiones de forma precisa.

## 📂 1. ESTRUCTURA DEL PROYECTO
A continuación se muestra un mapa visual de directorios y archivos de este proyecto (excluyendo entornos virtuales, librerías de dependencias y cachés):

```
📄 .env
📄 .gitignore
📄 analizador.py
📁 apis/
📄 app.log
📄 config.py
📄 copiar_para_ia.py
📁 ENTORN VISUAL/
  📄 CARETAS.BAT
  📁 Nueva carpeta/
📄 explorador.py
📄 generador_de_contexto_maestro.py
📄 generar_contexto.py
📄 historial.log
📁 logs/
  📁 errors/
    📄 errores.log
📄 MANUAL_MECANICO.md
📄 MASTER_CONTEXT2.md
📄 mecanico.py
📁 memoria/
  📁 errores/
    📄 errores.log
  📄 historial.log
  📁 sesiones/
  📄 token_log.json
📁 modulos/
  📄 analizador.py
  📄 autoeditor.py
  📄 bucle_mejora.py
  📄 buscador_web.py
  📄 explorador.py
  📄 generador.py
  📄 git_manager.py
  📄 github_reader.py
  📄 github_scout.py
  📄 lector_contexto.py
  📄 memoria_historial.py
  📁 Nueva carpeta/
    📄 asfasf.py
    📄 generador.py
    📄 mecanico (1).py
    📄 mecanico.py
    📄 token_monitor.py
  📄 nvidia_selector.py
  📄 orquestador.py
  📄 reinicio.py
  📄 reparador.py
  📄 revertir.py
  📄 tester.py
  📄 texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial.py
  📄 token_monitor.py
  📄 uptime.py
📄 orquestador.py
📁 proyectos/
📄 scanner_maestro.py
📄 uptime.py
📁 visual/
  📁 assets/
    📁 fonts/
    📁 icons/
  📁 components/
  📁 css/
  📁 data/
  📁 js/
  📁 logs/
  📁 pages/
  📁 templates/
  📁 themes/
```

## 📄 2. CONTENIDO DE ARCHIVOS CLAVE (CÓDIGO Y CONFIGURACIÓN)
A continuación se detallan los archivos clave del proyecto para comprender su inicialización, dependencias y lógica central:

### 📂 Archivo: `analizador.py`
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
    for raiz, dirs, archivos in os.walk(carpeta):
        dirs[:] = [d for d in dirs if d not in ["__pycache__", ".git", "node_modules"]]
        for archivo in archivos:
            if archivo.endswith(".py"):
                ruta = os.path.join(raiz, archivo)
                total_archivos += 1
                analisis = analizar_python(ruta)
                if "Errores: 0" not in analisis and not analisis.startswith("ERROR"):
                    total_errores += 1
                    reporte.append(analisis)
    resumen = f"ANÁLISIS DE PROYECTO: {carpeta}\n"
    resumen += f"Archivos Python analizados: {total_archivos}\n"
    resumen += f"Archivos con errores: {total_errores}\n"
    resumen += "=" * 40 + "\n"
    if reporte:
        resumen += "\n".join(reporte)
    else:
        resumen += "No se encontraron errores de sintaxis."
    return resumen

def analizar_con_ia(ruta: str, preguntar_fn) -> str:
    """Analiza un archivo con la ayuda de la inteligencia artificial."""
    codigo = leer_archivo(ruta)
    if codigo.startswith("ERROR"):
        return codigo
    prompt = f"""Analizá este código y encontrá:
1. Errores o bugs
2. Problemas de rendimiento
3. Mejoras posibles
4. Código duplicado

Archivo: {ruta}
Código:
{codigo[:3000]}

Respondé en español, sé conciso y directo."""
    return preguntar_fn(prompt)

def ejecutar(accion: str, texto: str) -> str:
    """Ejecuta la acción solicitada."""
    t = texto.lower()
    palabras = texto.split()

    if "proyecto" in t:
        carpeta = palabras[-1] if len(palabras) > 1 else BASE
        return analizar_proyecto(carpeta)
    elif "ia" in t or "inteligente" in t:
        ruta = palabras[-1] if len(palabras) > 1 else ""
        if not ruta or not os.path.exists(ruta):
            return "ERROR: Especifica la ruta del archivo. Ej: analizar ia C:/ruta/archivo.py"
        from mecanico import preguntar
        return analizar_con_ia(ruta, preguntar)
    elif "archivo" in t:
        ruta = palabras[-1] if len(palabras) > 1 else ""
        if not ruta or not os.path.exists(ruta):
            return "ERROR: Especifica la ruta del archivo. Ej: analizar archivo C:/ruta/archivo.py"
        return analizar_python(ruta)
    else:
        return "ERROR: Acción no reconocida. Opciones: proyecto, ia, archivo"

# Uso ejemplo
if __name__ == "__main__":
    print(ejecutar("accion", "analizar proyecto C:/IA/AGENTE/MECANICO"))
    print(ejecutar("accion", "analizar ia C:/rito/archivo.py"))
    print(ejecutar("accion", "analizar archivo C:/rito/archivo.py"))
```

### 📂 Archivo: `config.py`
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

### 📂 Archivo: `copiar_para_ia.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MECANICO IA - Copiador de archivos para chats de IAs.

Permite seleccionar archivos o partes de archivos y copiarlos
a un archivo TXT listo para pegar en chats de IAs.
"""

import os
import sys
from pathlib import Path

# ============================================
# CONFIGURACIÓN
# ============================================

BASE_DIR = Path(r"C:\IA\AGENTE\mecanico beta prueva\mecanico_v2")
OUTPUT_FILE = BASE_DIR / "PARA_PEGAR_EN_IA.txt"

# ============================================
# FUNCIONES DE UTILIDAD
# ============================================

def limpiar_pantalla():
    """Limpia la pantalla de terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def esperar_tecla():
    """Espera a que el usuario presione una tecla."""
    input("\nPresiona Enter para continuar...")


def mostrar_menu():
    """Muestra el menú principal."""
    limpiar_pantalla()
    print("=" * 50)
    print("   MECANICO IA - Copiador para IAs")
    print("=" * 50)
    print()
    print("  1. Copiar archivo completo")
    print("  2. Copiar parte de un archivo (líneas X a Y)")
    print("  3. Listar archivos de una carpeta")
    print("  4. Ver contenido del TXT actual")
    print("  5. Borrar TXT y empezar de nuevo")
    print("  6. Salir")
    print("  7. Copiar MULTIPLES archivos de una vez")
    print()
    print("=" * 50)
    print(f"  TXT destino: {OUTPUT_FILE}")
    print("=" * 50)
    print()


def copiar_archivo_a_txt(ruta: str) -> bool:
    """Copia un archivo al TXT. Retorna True si tuvo éxito."""
    archivo = BASE_DIR / ruta

    if not archivo.exists():
        print(f"[ERROR] No existe: {archivo}")
        return False

    with open(OUTPUT_FILE, "a", encoding="utf-8") as out:
        out.write("\n")
        out.write("=" * 60 + "\n")
        out.write(f"ARCHIVO: {ruta}\n")
        out.write("=" * 60 + "\n")
        out.write("\n")

        with open(archivo, "r", encoding="utf-8") as f:
            out.write(f.read())

        out.write("\n")

    print(f"[OK] Archivo copiado: {ruta}")
    return True


def copiar_archivo_completo():
    """Copia un archivo completo al TXT."""
    limpiar_pantalla()
    print("=" * 50)
    print("   COPIAR ARCHIVO COMPLETO")
    print("=" * 50)
    print()
    print(f"  Ruta base: {BASE_DIR}")
    print()
    print("  Ejemplos:")
    print("    core\\orchestrator.py")
    print("    config\\settings.py")
    print("    utils\\logging\\terminal_logger.py")
    print("    main.py")
    print()

    ruta = input("Ruta del archivo (relativa a base): ").strip()
    if not ruta:
        return

    if copiar_archivo_a_txt(ruta):
        print(f"[OK] Guardado en: {OUTPUT_FILE}")

    esperar_tecla()


def copiar_multiples_archivos():
    """Copia múltiples archivos de una sola vez al TXT."""
    limpiar_pantalla()
    print("=" * 50)
    print("   COPIAR MULTIPLES ARCHIVOS")
    print("=" * 50)
    print()
    print(f"  Ruta base: {BASE_DIR}")
    print()
    print("  Escribí las rutas separadas por comas.")
    print("  Ejemplo:")
    print("    core\\orchestrator.py, config\\settings.py, utils\\logging\\terminal_logger.py")
    print()
    print("  O presioná Enter para ver la lista de archivos disponibles.")
    print()

    entrada = input("Rutas (separadas por comas): ").strip()

    if not entrada:
        # Mostrar lista de archivos .py disponibles
        print("\n  Archivos .py disponibles:")
        print("-" * 50)
        archivos = sorted(BASE_DIR.rglob("*.py"))
        for i, py_file in enumerate(archivos, 1):
            rel_path = py_file.relative_to(BASE_DIR)
            print(f"  {i:3d}. {rel_path}")
        print("-" * 50)
        print("\n  Copiá los números separados por comas.")
        print("  Ejemplo: 1, 5, 12")
        print()

        numeros = input("Números de archivos: ").strip()
        if not numeros:
            return

        seleccionados = []
        for num_str in numeros.split(","):
            try:
                idx = int(num_str.strip()) - 1
                if 0 <= idx < len(archivos):
                    rel_path = archivos[idx].relative_to(BASE_DIR)
                    seleccionados.append(str(rel_path))
            except ValueError:
                pass

        if not seleccionados:
            print("[ERROR] Ningún archivo válido seleccionado")
            esperar_tecla()
            return

        rutas = seleccionados
    else:
        rutas = [r.strip() for r in entrada.split(",")]

    print(f"\n  Copiando {len(rutas)} archivo(s)...")
    print()

    exitosos = 0
    fallidos = 0

    for ruta in rutas:
        if copiar_archivo_a_txt(ruta):
            exitosos += 1
        else:
            fallidos += 1

    print()
    print(f"[OK] Exitosos: {exitosos} | Fallidos: {fallidos}")
    print(f"[OK] Todo guardado en: {OUTPUT_FILE}")
    esperar_tecla()


def copiar_parte_archivo():
    """Copia líneas específicas de un archivo al TXT."""
    limpiar_pantalla()
    print("=" * 50)
    print("   COPIAR PARTE DE UN ARCHIVO")
    print("=" * 50)
    print()

    ruta = input("Ruta del archivo (relativa a base): ").strip()
    if not ruta:
        return

    archivo = BASE_DIR / ruta

    if not archivo.exists():
        print(f"\n[ERROR] No existe: {archivo}")
        esperar_tecla()
        return

    # Mostrar líneas numeradas
    print("\n  Líneas del archivo:")
    print("-" * 50)
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    for i, linea in enumerate(lineas, 1):
        print(f"  {i:4d} | {linea.rstrip()}")

    print("-" * 50)
    print()

    try:
        inicio = int(input("Línea inicial: ").strip())
        fin = int(input("Línea final: ").strip())
    except ValueError:
        print("\n[ERROR] Números inválidos")
        esperar_tecla()
        return

    with open(OUTPUT_FILE, "a", encoding="utf-8") as out:
        out.write("\n")
        out.write("=" * 60 + "\n")
        out.write(f"ARCHIVO: {ruta} (líneas {inicio} a {fin})\n")
        out.write("=" * 60 + "\n")
        out.write("\n")

        for i in range(inicio - 1, min(fin, len(lineas))):
            out.write(lineas[i])

        out.write("\n")

    print(f"\n[OK] Líneas {inicio} a {fin} copiadas de {ruta}")
    esperar_tecla()


def listar_carpeta():
    """Lista los archivos .py de una carpeta en el TXT."""
    limpiar_pantalla()
    print("=" * 50)
    print("   LISTAR ARCHIVOS DE CARPETA")
    print("=" * 50)
    print()

    carpeta = input("Nombre de carpeta (ej: core, utils, modules): ").strip()
    if not carpeta:
        return

    ruta_carpeta = BASE_DIR / carpeta

    if not ruta_carpeta.exists():
        print(f"\n[ERROR] No existe: {ruta_carpeta}")
        esperar_tecla()
        return

    with open(OUTPUT_FILE, "a", encoding="utf-8") as out:
        out.write("\n")
        out.write("=" * 60 + "\n")
        out.write(f"CARPETA: {carpeta}\n")
        out.write("=" * 60 + "\n")
        out.write("\n")

        for py_file in sorted(ruta_carpeta.rglob("*.py")):
            rel_path = py_file.relative_to(BASE_DIR)
            out.write(f"  {rel_path}\n")

        out.write("\n")

    print(f"\n[OK] Lista de archivos de {carpeta} copiada")
    esperar_tecla()


def ver_txt():
    """Muestra el contenido del TXT actual."""
    limpiar_pantalla()
    print("=" * 50)
    print("   CONTENIDO DEL TXT ACTUAL")
    print("=" * 50)
    print()

    if not OUTPUT_FILE.exists():
        print("[INFO] El archivo no existe todavía.")
        esperar_tecla()
        return

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        print(f.read())

    print()
    esperar_tecla()


def borrar_txt():
    """Borra el TXT para empezar de nuevo."""
    limpiar_pantalla()
    print("=" * 50)
    print("   BORRAR TXT Y EMPEZAR DE NUEVO")
    print("=" * 50)
    print()

    if OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()
        print("[OK] TXT borrado.")
    else:
        print("[INFO] No había TXT para borrar.")

    esperar_tecla()


def salir():
    """Sale del programa."""
    print()
    print("[OK] Hasta luego.")
    sys.exit(0)


# ============================================
# MENU PRINCIPAL
# ============================================

def main():
    """Loop principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Elegí 1, 2, 3, 4, 5, 6 o 7: ").strip()

        if opcion == "1":
            copiar_archivo_completo()
        elif opcion == "2":
            copiar_parte_archivo()
        elif opcion == "3":
            listar_carpeta()
        elif opcion == "4":
            ver_txt()
        elif opcion == "5":
            borrar_txt()
        elif opcion == "6":
            salir()
        elif opcion == "7":
            copiar_multiples_archivos()
        else:
            print("\n[ERROR] Opción no válida")
            esperar_tecla()


# ============================================
# ARRANQUE
# ============================================

if __name__ == "__main__":
    main()

```

### 📂 Archivo: `explorador.py`
```python
import os
import shutil
import datetime

def listar(ruta):
    """
    Lista el contenido de una carpeta.

    Args:
        ruta (str): La ruta de la carpeta.

    Returns:
        str: Un mensaje con el contenido de la carpeta.
    """
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
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
    """
    Busca archivos que contengan un patrón en una carpeta y sus subcarpetas.

    Args:
        ruta (str): La ruta de la carpeta.
        patron (str): El patrón a buscar.

    Returns:
        str: Un mensaje con los archivos encontrados.
    """
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    encontrados = []
    for raiz, dirs, archivos in os.walk(ruta):
        dirs[:] = [d for d in dirs if d not in ["__pycache__", ".git", "node_modules"]]
        for archivo in archivos:
            if patron.lower() in archivo.lower():
                ruta_completa = os.path.join(raiz, archivo)
                encontrados.append(ruta_completa)
    if not encontrados:
        return f"No se encontro '{patron}' en {ruta}"
    return f"Encontrados {len(encontrados)} archivos:\n" + "\n".join(encontrados[:20])

def crear_carpeta(ruta):
    """
    Crea una carpeta.

    Args:
        ruta (str): La ruta de la carpeta.

    Returns:
        str: Un mensaje con el resultado de la operación.
    """
    try:
        os.makedirs(ruta, exist_ok=True)
        return f"OK Carpeta creada: {ruta}"
    except Exception as e:
        return f"ERROR: {e}"

def copiar(origen, destino):
    """
    Copia un archivo o carpeta.

    Args:
        origen (str): La ruta del archivo o carpeta original.
        destino (str): La ruta del archivo o carpeta destino.

    Returns:
        str: Un mensaje con el resultado de la operación.
    """
    try:
        if os.path.isdir(origen):
            shutil.copytree(origen, destino)
        else:
            shutil.copy2(origen, destino)
        return f"OK Copiado: {origen} -> {destino}"
    except Exception as e:
        return f"ERROR: {e}"

def mover(origen, destino):
    """
    Mueve un archivo o carpeta.

    Args:
        origen (str): La ruta del archivo o carpeta original.
        destino (str): La ruta del archivo o carpeta destino.

    Returns:
        str: Un mensaje con el resultado de la operación.
    """
    try:
        shutil.move(origen, destino)
        return f"OK Movido: {origen} -> {destino}"
    except Exception as e:
        return f"ERROR: {e}"

def leer(ruta):
    """
    Lee el contenido de un archivo.

    Args:
        ruta (str): La ruta del archivo.

    Returns:
        str: Un mensaje con el contenido del archivo.
    """
    if not os.path.exists(ruta):
        return f"ERROR: Archivo no encontrado: {ruta}"
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
        lineas = contenido.split("\n")
        if len(lineas) > 50:
            return f"Primeras 50 lineas de {ruta}:\n" + "\n".join(lineas[:50]) + f"\n...({len(lineas)} lineas total)"
        return f"Contenido de {ruta}:\n{contenido}"
    except Exception as e:
        return f"ERROR: {e}"

def info(ruta):
    """
    Muestra información sobre un archivo o carpeta.

    Args:
        ruta (str): La ruta del archivo o carpeta.

    Returns:
        str: Un mensaje con la información del archivo o carpeta.
    """
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    stat = os.stat(ruta)
    modificado = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    size = stat.st_size
    size_str = f"{size} bytes" if size < 1024 else f"{round(size/1024/1024, 2)} MB"
    tipo = "Carpeta" if os.path.isdir(ruta) else "Archivo"
    return f"Info de {ruta}:\nTipo: {tipo}\nTamanio: {size_str}\nModificado: {modificado}"

def ejecutar(accion, texto):
    """
    Ejecuta una acción según el texto ingresado.

    Args:
        accion (str): La acción a realizar.
        texto (str): El texto ingresado.

    Returns:
        str: Un mensaje con el resultado de la acción.
    """
    palabras = texto.split()
    t = texto.lower()

    if "listar" in t or "ver" in t or "mostrar" in t:
        ruta = palabras[-1] if len(palabras) > 1 else "C:/"
        return listar(ruta)

    elif "buscar" in t:
        if len(palabras) >= 3:
            patron = palabras[-2]
            ruta = palabras[-1]
        else:
            return "ERROR: Uso: explorar buscar patron C:/ruta"
        return buscar(ruta, patron)

    elif "crear carpeta" in t:
        ruta = palabras[-1]
        return crear_carpeta(ruta)

    elif "copiar" in t:
        if len(palabras) >= 3:
            return copiar(palabras[-2], palabras[-1])
        return "ERROR: Uso: explorar copiar origen destino"

    elif "mover" in t:
        if len(palabras) >= 3:
            return mover(palabras[-2], palabras[-1])
        return "ERROR: Uso: explorar mover origen destino"

    elif "leer" in t:
        if len(palabras) >= 2:
            ruta = palabras[-1]
            return leer(ruta)
        return "ERROR: Uso: explorar leer C:/ruta"

    elif "info" in t:
        if len(palabras) >= 2:
            ruta = palabras[-1]
            return info(ruta)
        return "ERROR: Uso: explorar info C:/ruta"

    else:
        return "ERROR: Acción no reconocida."
```

### 📂 Archivo: `generador_de_contexto_maestro.py`
```python
import os
import datetime
from pathlib import Path

# --- CONFIGURACIÓN GENERAL ---
# Extensiones de archivos de texto/código que vale la pena documentar completos
TEXT_EXTENSIONS = {
    '.py', '.js', '.ts', '.tsx', '.jsx', '.json', '.yaml', '.yml', 
    '.toml', '.md', '.txt', '.conf', '.env.example', '.ini', '.cfg',
    '.html', '.css', '.sh', '.bat', '.ps1', '.go', '.rs', '.java', '.c', '.cpp', '.h'
}

# Carpetas críticas que NUNCA debemos escanear o leer para no saturar el contexto
IGNORE_DIRS = {
    "venv", ".venv", "env", "node_modules", ".git", "__pycache__", 
    "backups", "dist", "build", "out", ".next", ".nuxt", ".cache",
    "whisper_models", "workspace", "session", ".wwebjs_cache",
    "Cache", "Code Cache", "GPUCache", "GrShaderCache", "DawnGraphiteCache", 
    "DawnWebGPUCache", "IndexedDB", "Local Storage", "Service Worker"
}

# Archivos específicos que debemos ignorar para evitar duplicar información o bucles
IGNORE_FILES = {
    "MASTER_CONTEXT.md", "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "generador_contexto.py"
}

# Límite de caracteres por archivo para no saturar la ventana de contexto de la IA
MAX_FILE_CHARS = 20000

def leer_archivo_seguro(path: Path) -> str:
    """Intenta leer un archivo de texto con distintas codificaciones de forma segura."""
    for encoding in ("utf-8", "latin-1", "utf-16", "cp1252"):
        try:
            return path.read_text(encoding=encoding, errors="ignore")
        except Exception:
            continue
    return ""

def generar_arbol_visual(root: Path) -> list:
    """Genera una representación visual limpia del directorio ignorando rutas basura."""
    tree_lines = []
    # Usamos rglob para recorrer todos los archivos de manera recursiva de forma ordenada
    for path in sorted(root.rglob("*")):
        # Filtrar si alguna de las partes de la ruta está en la lista de ignorados
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.name in IGNORE_FILES:
            continue
            
        rel = path.relative_to(root)
        indent = "  " * (len(rel.parts) - 1)
        
        if path.is_dir():
            tree_lines.append(f"{indent}📁 {rel.name}/")
        else:
            tree_lines.append(f"{indent}📄 {rel.name}")
            
    return tree_lines

def obtener_archivos_clave(root: Path) -> list:
    """Busca dinámicamente archivos clave de configuración, documentación y código."""
    archivos_clave = []
    
    # Patrones de archivos que son de alta prioridad (configuraciones globales, lecturas iniciales)
    patrones_alta_prioridad = [
        "README.md", "requirements.txt", "package.json", "Makefile",
        "docker-compose.yml", "Dockerfile", ".env.example", "config.py",
        "pyproject.toml", "setup.py"
    ]
    
    for path in sorted(root.rglob("*")):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.name in IGNORE_FILES:
            continue
            
        if path.is_file():
            rel_str = str(path.relative_to(root)).replace("\\", "/")
            
            # 1. Agregar si coincide con patrones de alta prioridad
            if any(path.name.lower() == p.lower() for p in patrones_alta_prioridad):
                archivos_clave.append(path)
                continue
                
            # 2. Agregar si tiene una extensión de código válida y no es gigante
            if path.suffix in TEXT_EXTENSIONS:
                # Filtrar si está en carpetas de assets, tests o temporales muy profundas si se desea
                archivos_clave.append(path)
                
    return archivos_clave

def generar_master_context():
    root = Path(__file__).parent.resolve()
    nombre_proyecto = root.name
    output_file = root / "MASTER_CONTEXT.md"
    
    output_lines = []
    output_lines.append(f"# 🧠 MASTER CONTEXT - {nombre_proyecto.upper()}")
    output_lines.append(f"Generado automáticamente el: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    output_lines.append(
        "Este archivo consolida la estructura, los archivos fuente principales y la lógica "
        "del proyecto para que cualquier IA pueda entender su contexto global inmediatamente "
        "y proponer modificaciones, depuraciones o extensiones de forma precisa.\n"
    )
    
    # 1. ESTRUCTURA DEL PROYECTO
    output_lines.append("## 📂 1. ESTRUCTURA DEL PROYECTO")
    output_lines.append("A continuación se muestra un mapa visual de directorios y archivos de este proyecto (excluyendo entornos virtuales, librerías de dependencias y cachés):\n")
    
    tree = generar_arbol_visual(root)
    output_lines.append("```")
    output_lines.extend(tree)
    output_lines.append("```\n")
    
    # 2. CONTENIDO DE ARCHIVOS CLAVE
    output_lines.append("## 📄 2. CONTENIDO DE ARCHIVOS CLAVE (CÓDIGO Y CONFIGURACIÓN)")
    output_lines.append("A continuación se detallan los archivos clave del proyecto para comprender su inicialización, dependencias y lógica central:\n")
    
    archivos = obtener_archivos_clave(root)
    
    for path in archivos:
        rel_path = path.relative_to(root)
        output_lines.append(f"### 📂 Archivo: `{rel_path}`")
        
        # Determinar el resaltador de sintaxis Markdown
        ext = path.suffix.lower().replace(".", "")
        if ext in ("py", "python"):
            lang = "python"
        elif ext in ("js", "javascript"):
            lang = "javascript"
        elif ext in ("ts", "typescript"):
            lang = "typescript"
        elif ext in ("json", "yml", "yaml", "toml", "md", "html", "css", "sh", "sql"):
            lang = ext
        else:
            lang = "text"
            
        output_lines.append(f"```{lang}")
        
        content = leer_archivo_seguro(path)
        if len(content) > MAX_FILE_CHARS:
            mitad = MAX_FILE_CHARS // 2
            output_lines.append(content[:mitad])
            output_lines.append(f"\n\n--- [CONTENIDO TRUNCADO POR TAMAÑO EXCESIVO (> {MAX_FILE_CHARS} caracteres)] ---\n")
            output_lines.append(content[-5000:])
        else:
            output_lines.append(content)
            
        output_lines.append("```\n")
        
    # 3. DIRECTRICES DE DESARROLLO (Instrucciones universales para IA)
    output_lines.append("## 🤖 3. DIRECTRICES DE DESARROLLO E INSTRUCCIONES PARA LA IA")
    output_lines.append(
        "Al sugerir cambios, resolver bugs o escribir nuevas características para este proyecto, "
        "debes respetar las siguientes reglas obligatorias:\n"
    )
    output_lines.append("1. **Respetar Rutas:** Trabaja siempre bajo el esquema de archivos y carpetas definido en la sección de estructura.")
    output_lines.append("2. **Consistencia de Estilo:** Analiza los lenguajes, tabulaciones y el estilo de programación usado en los archivos mostrados antes de generar nuevas líneas de código.")
    output_lines.append("3. **Gestión de Dependencias:** Si necesitas librerías externas adicionales, no las importes directamente sin advertir al usuario. Indica explícitamente qué dependencias deben agregarse en los archivos correspondientes (por ejemplo, `requirements.txt` o `package.json`).")
    output_lines.append("4. **Seguridad y Credenciales:** Nunca expongas ni guardes contraseñas, tokens o claves API directamente en el código de producción. Promueve siempre el uso de variables de entorno (ej: `.env`).")
    output_lines.append("5. **Formato de Entrega de Código:** Cuando propongas modificaciones o código nuevo, especifica la ruta destino en un comentario en la cabecera del bloque de código (ej: `# /ruta/al/archivo.py` o `// /ruta/al/archivo.js`).")
    output_lines.append("6. **Evitar Código Fantasma:** No dejes funciones a medias con comentarios `// agregar lógica aquí` o `pass`. Si reescribes una estructura de código, asegúrate de que sea funcional y esté autocontenida.")

    # Guardar en archivo final
    try:
        output_file.write_text("\n".join(output_lines), encoding="utf-8")
        print("✅ ¡Listo! El contexto maestro se generó exitosamente.")
        print(f"👉 Archivo guardado en: {output_file.resolve()}")
        print("\n💡 PRÓXIMO PASO: Abre 'MASTER_CONTEXT.md', copia su contenido y pégalo al iniciar tu conversación con cualquier IA.")
    except Exception as e:
        print(f"❌ Error al escribir el archivo de salida: {e}")

if __name__ == "__main__":
    generar_master_context()
```

### 📂 Archivo: `generar_contexto.py`
```python
import os
import json
import datetime

BASE = "C:/IA/AGENTE/MECANICO"
OUTPUT = "C:/IA/AGENTE/MECANICO/MASTER_CONTEXT2.md"

def leer_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        return ""

def generar_contexto():
    md = []
    md.append(f"# MASTER CONTEXT - MECANICO IA")
    md.append(f"Generado: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    # Estructura
    md.append("## ESTRUCTURA")
    md.append("```")
    for raiz, dirs, archivos in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ["__pycache__", ".git", "node_modules", "backups"]]
        nivel = raiz.replace(BASE, "").count(os.sep)
        indent = "  " * nivel
        md.append(f"{indent}{os.path.basename(raiz)}/")
        for archivo in archivos:
            md.append(f"{indent}  {archivo}")
    md.append("```\n")

    # Modulos
    md.append("## MODULOS")
    carpeta_modulos = os.path.join(BASE, "modulos")
    for archivo in sorted(os.listdir(carpeta_modulos)):
        if archivo.endswith(".py") and not archivo.startswith("_"):
            ruta = os.path.join(carpeta_modulos, archivo)
            contenido = leer_archivo(ruta)
            md.append(f"\n### {archivo}")
            md.append(f"```python\n{contenido[:2000]}\n```")

    # Config
    md.append("\n## CONFIG")
    md.append(f"```python\n{leer_archivo(os.path.join(BASE, 'config.py'))}\n```")

    # Mecanico principal (solo estructura)
    md.append("\n## MECANICO.PY - TRIGGERS ACTIVOS")
    mecanico = leer_archivo(os.path.join(BASE, "mecanico.py"))
    triggers = [l.strip() for l in mecanico.split("\n") if "startswith(" in l]
    for t in triggers:
        md.append(f"- {t}")

    # APIs disponibles
    md.append("\n## APIS CONFIGURADAS")
    md.append("- groq: llama-3.3-70b-versatile")
    md.append("- gemini: gemini-2.5-flash")
    md.append("- cerebras: gpt-oss-120b")
    md.append("- nvidia: moonshotai/kimi-k2.6 (fallback: mistral-large, nemotron, deepseek-v4, llama-3.3)")
    md.append("- zai: glm-4.7-flash")
    md.append("- ollama: gemma3:4b (local)")

    # Pendientes
    md.append("\n## PENDIENTES PROXIMA SESION")
    md.append("- Arreglar orquestador (devuelve None en pedidos complejos)")
    md.append("- Implementar Headoom MCP")
    md.append("- Implementar CodeBase Memory MCP")
    md.append("- Auto-reparacion y auto-mejora de MECANICO")
    md.append("- Estabilizar modo Auto (orquestador)")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"OK Contexto generado: {OUTPUT}")

generar_contexto()

```

### 📂 Archivo: `MANUAL_MECANICO.md`
```md
# 🔧 MANUAL DE USO - MECANICO IA

## ¿Qué es MECANICO?
MECANICO es un agente IA especializado en analizar, reparar y mejorar código.
Usa múltiples APIs de IA (Groq, Gemini, Cerebras, Ollama) y puede trabajar
en cualquier proyecto de tu PC.

---

## 🚀 Cómo arrancar

```
cd C:\IA\AGENTE\MECANICO
python mecanico.py
```

---

## 📋 Modos disponibles

| Modo | Descripción |
|------|-------------|
| **1. Manual** | Vos le decís qué hacer |
| **2. Auto** | MECANICO trabaja solo (en construcción) |
| **3. Consenso** | Todas las APIs responden juntas |
| **4. Ver APIs** | Estado de las APIs conectadas |

---

## 💬 Comandos en Modo Manual

### 🔍 ANALIZAR
Analiza archivos o proyectos buscando errores de sintaxis.

```
analizar C:/ruta/archivo.py
analizar proyecto C:/ruta/proyecto
analizar ia C:/ruta/archivo.py     ← usa IA para análisis profundo
```

### 🔧 REPARAR
Repara un archivo usando IA. Hace backup automático antes.

```
reparar C:/ruta/archivo.py
```

### ↩️ REVERTIR
Restaura un archivo a su versión anterior.

```
revertir mecanico.py               ← revierte al backup más reciente
revertir listar mecanico.py        ← muestra backups disponibles
```

### 📁 EXPLORAR (próximamente)
Navega y trabaja con cualquier carpeta del sistema.

```
explorar listar C:/ruta
explorar buscar archivo.py C:/ruta
explorar leer C:/ruta/archivo.py
explorar info C:/ruta/archivo.py
explorar copiar origen destino
explorar mover origen destino
```

### 🤖 EJECUTAR JSON (Autoeditor)
Crea o modifica archivos usando IA. El comando más poderoso.

#### Crear un módulo nuevo:
```
ejecutar json {"accion": "crear_modulo", "archivo": "modulos/nuevo.py", "contenido": "codigo aqui", "backup": false}
```

#### Crear un archivo:
```
ejecutar json {"accion": "crear_archivo", "archivo": "workspace/notas.txt", "contenido": "contenido aqui", "backup": false}
```

#### Modificar un archivo con IA:
```
ejecutar json {"accion": "modificar_con_ia", "archivo": "modulos/archivo.py", "descripcion": "que queres que cambie", "backup": true}
```

#### Leer un archivo:
```
ejecutar json {"accion": "leer_archivo", "archivo": "config.py"}
```

### 🔀 GIT
Operaciones de Git integradas.

```
git estado        ← ver qué cambió
git push          ← subir todo a GitHub
git historial     ← ver últimos commits
git commit        ← hacer commit sin push
```

### 📊 APIS
Ver el estado de todas las APIs.

```
apis
```

### 🌐 CONSENSO
Preguntarle a todas las APIs al mismo tiempo.
Elegí la opción **3** en el menú.

---

## 🔑 APIs disponibles

| API | Modelo | Velocidad | Uso |
|-----|--------|-----------|-----|
| **Groq** | llama-3.3-70b | ⚡⚡⚡ muy rápido | Respuestas rápidas |
| **Gemini** | gemini-2.5-flash | ⚡⚡ rápido | Análisis complejo |
| **Cerebras** | gpt-oss-120b | ⚡⚡ rápido | Alternativa potente |
| **Ollama** | gemma3:4b | ⚡ local | Sin internet, privado |

---

## 📂 Estructura de carpetas

```
C:\IA\AGENTE\MECANICO\
├── mecanico.py          ← núcleo principal
├── config.py            ← configuración y APIs
├── .env                 ← API keys (nunca compartir)
├── modulos\
│   ├── autoeditor.py    ← crea y modifica archivos con IA
│   ├── analizador.py    ← analiza proyectos
│   ├── reparador.py     ← repara código con IA
│   ├── revertir.py      ← restaura backups
│   ├── git_manager.py   ← maneja Git
│   └── explorador.py    ← navega el sistema
├── memoria\
│   ├── backups\         ← copias antes de cada cambio
│   ├── errores\         ← log de errores
│   └── sesiones\        ← historial
└── workspace\           ← carpeta de trabajo
```

---

## ⚠️ Reglas importantes

1. **MECANICO nunca borra archivos** sin confirmación
2. **Siempre hace backup** antes de modificar
3. **Si algo falla** → usar `revertir archivo.py`
4. **Los errores** se guardan en `memoria/errores/errores.log`
5. **Cada cambio** se guarda en Git automáticamente

---

## 🆘 Si algo sale mal

**Ver el log de errores:**
```
type C:\IA\AGENTE\MECANICO\memoria\errores\errores.log
```

**Revertir un archivo:**
```
revertir mecanico.py
```

**Ver historial de Git:**
```
cd C:\IA\AGENTE\MECANICO
git log --oneline
```

**Volver a una versión anterior en Git:**
```
git checkout HASH -- archivo.py
```

---

## 💡 Ejemplos de uso real

**Analizar y reparar MAT.ONE:**
```
analizar proyecto C:/IA/AGENTE/MAT.ONE
reparar C:/IA/AGENTE/MAT.ONE/mat_one.py
```

**Crear un módulo nuevo:**
```
ejecutar json {"accion": "crear_modulo", "archivo": "modulos/nuevo.py", "contenido": "def ejecutar(accion, texto):\n    return 'hola'", "backup": false}
```

**Modificar config con IA:**
```
ejecutar json {"accion": "modificar_con_ia", "archivo": "config.py", "descripcion": "Agregar nueva API llamada zai con modelo zai-glm-4.7", "backup": true}
```

```

### 📂 Archivo: `MASTER_CONTEXT2.md`
```md
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
    for item in sorted(ite


--- [CONTENIDO TRUNCADO POR TAMAÑO EXCESIVO (> 20000 caracteres)] ---

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
```

### 📂 Archivo: `mecanico.py`
```python
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
    except Exception:
        pass
    print(Fore.RED + f"\n[ERROR] {error}")
    print(Fore.YELLOW + f"[LOG] Guardado en {LOG_FILE}")

def registrar_tokens(api, tokens_input, tokens_output):
    try:
        from modulos import token_monitor
        token_monitor.registrar_uso(api, tokens_input, tokens_output)
    except Exception:
        pass

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
                print(Fore.RED + f"  ERROR {nombre}: {e}")

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
                except Exception:
                    pass
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
                    model=config["modelo"],
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=2000
                )
                resultados[nombre] = respuesta.choices[0].message.content
                uso = respuesta.usage
                registrar_tokens(nombre, uso.prompt_tokens, uso.completion_tokens)

            elif nombre == "gemini":
                from google import genai
                client = genai.Client(api_key=config["key"])
                respuesta = client.models.generate_content(model=config["modelo"], contents=prompt)
                resultados[nombre] = respuesta.text
                try:
                    meta = respuesta.usage_metadata
                    registrar_tokens(nombre, meta.prompt_token_count, meta.candidates_token_count)
                except Exception:
                    registrar_tokens(nombre, len(prompt)//4, len(respuesta.text)//4)

            elif nombre == "cerebras":
                from cerebras.cloud.sdk import Cerebras
                client = Cerebras(api_key=config["key"])
                respuesta = client.chat.completions.create(
                    model=config["modelo"],
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=2000
                )
                resultados[nombre] = respuesta.choices[0].message.content
                uso = respuesta.usage
                registrar_tokens(nombre, uso.prompt_tokens, uso.completion_tokens)

            elif nombre == "nvidia":
                headers = {
                    "Authorization": f"Bearer {config['key']}",
                    "Content-Type": "application/json"
                }
                body = {
                    "model": config["modelo"],
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 2000,
                    "stream": False
                }
                r = requests.post(
                    "https://integrate.api.nvidia.com/v1/chat/completions",
                    headers=headers,
                    json=body,
                    timeout=60
                )
                try:
                    data = r.json()
                    contenido = data["choices"][0]["message"]["content"]
                    if "<think>" in contenido and "</think>" in contenido:
                        contenido = contenido.split("</think>")[-1].strip()
                    resultados[nombre] = contenido
                    uso = data.get("usage", {})
                    registrar_tokens(nombre, uso.get("prompt_tokens", 0), uso.get("completion_tokens", 0))
                except Exception:
                    resultados[nombre] = f"ERROR parseando respuesta NVIDIA: {r.text[:300]}"

            elif nombre == "zai":
                headers = {"Authorization": config["key"], "Content-Type": "application/json"}
                body = {"model": config["modelo"], "messages": [{"role": "user", "content": prompt}], "max_tokens": 2000}
                r = requests.post("https://open.bigmodel.cn/api/paas/v4/chat/completions", headers=headers, json=body, timeout=30)
                data = r.json()
                resultados[nombre] = data["choices"][0]["message"]["content"]
                try:
                    uso = data.get("usage", {})
                    registrar_tokens(nombre, uso.get("prompt_tokens", 0), uso.get("completion_tokens", 0))
                except Exception:
                    pass

            elif nombre == "ollama":
                import ollama as ol
                respuesta = ol.chat(model=config["modelo"], messages=[{"role": "user", "content": prompt}])
                resultados[nombre] = respuesta["message"]["content"]
                try:
                    registrar_tokens(nombre, respuesta.get("prompt_eval_count", 0), respuesta.get("eval_count", 0))
                except Exception:
                    pass

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
    print(Fore.CYAN + "   MECANICO IA - Agente Reparador")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "  1. Modo Manual    - vos le decis que hacer")
    print(Fore.WHITE + "  2. Modo Auto      - lenguaje natural, MECANICO arma el plan")
    print(Fore.WHITE + "  3. Modo Consenso  - todas las APIs juntas")
    print(Fore.WHITE + "  4. Ver APIs       - estado de las APIs")
    print(Fore.WHITE + "  5. Cambiar API    - elegir con que IA trabajar")
    print(Fore.WHITE + "  s. Salir")
    print(Fore.CYAN + "=" * 55)

def mostrar_menu_apis():
    from config import APIS
    print()
    print(Fore.CYAN + "=" * 55)
    print(Fore.CYAN + "   Elegir API activa")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "  0. Auto (groq > gemini > cerebras > nvidia > zai > ollama)")
    apis = list(APIS.items())
    for i, (nombre, config) in enumerate(apis, 1):
        tiene_key = bool(config["key"]) or nombre == "ollama"
        estado = Fore.GREEN + "OK" if (config["activa"] and tiene_key) else Fore.RED + "OFF"
        print(f"  {i}. {estado} {nombre:<12} {config['modelo']}")
    print(Fore.CYAN + "=" * 55)
    return apis

def elegir_api():
    apis = mostrar_menu_apis()
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

def ver_


--- [CONTENIDO TRUNCADO POR TAMAÑO EXCESIVO (> 20000 caracteres)] ---

r"):
                    if "tester" in MODULOS:
                        resultado = MODULOS["tester"].ejecutar("tester", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial"):
                    if "texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial" in MODULOS:
                        resultado = MODULOS["texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial"].ejecutar("texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("memoria_historial"):
                    if "memoria_historial" in MODULOS:
                        resultado = MODULOS["memoria_historial"].ejecutar("memoria_historial", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue
                try:
                    print(Fore.WHITE + "Pensando...", end="", flush=True)
                    inicio = time.time()
                    respuesta = preguntar(hacer_prompt(entrada, api_actual), api=api_actual)
                    fin = round(time.time() - inicio, 2)
                    print(Fore.GREEN + f"\rMECANICO [{api_actual}] ({fin}s): " + Fore.WHITE + respuesta)
                except Exception as e:
                    guardar_error(str(e), "Modo manual")

        elif opcion == "2":
            print(Fore.GREEN + "\nModo Auto activado.")
            print(Fore.WHITE + "Decime en lenguaje natural que queres que haga.")
            print(Fore.WHITE + "Ej: 'andá a mi proyecto X, analizalo y arreglá lo que este roto'")
            print(Fore.WHITE + "Escribi 'menu' para volver.")
            print(Fore.CYAN + "-" * 55)

            while True:
                try:
                    pedido = input(Fore.YELLOW + "\nQue necesitas: ").strip()
                except KeyboardInterrupt:
                    break

                if not pedido:
                    continue
                if pedido.lower() == "menu":
                    break
                if pedido.lower() == "salir":
                    sys.exit(0)

                if "orquestador" not in MODULOS:
                    print(Fore.RED + "\nERROR: modulo orquestador no encontrado")
                    continue

                try:
                    print(Fore.WHITE + "Armando plan...", end="", flush=True)
                    pasos, explicacion, modelo_usado = MODULOS["orquestador"].armar_plan(pedido, preguntar)
                    print("\r" + " " * 30 + "\r", end="")

                    if not pasos:
                        print(Fore.YELLOW + f"\nMECANICO: {explicacion}")
                        continue

                    print(Fore.CYAN + f"\n[Plan armado por: {modelo_usado}]")
                    print(Fore.WHITE + f"\nResumen: {explicacion}\n")
                    print(Fore.WHITE + "Pasos a ejecutar:")
                    for i, paso in enumerate(pasos, 1):
                        print(Fore.WHITE + f"  {i}. {paso}")

                    confirmar = input(Fore.YELLOW + "\nEjecutar este plan? (s/n): ").strip().lower()
                    if confirmar != "s":
                        print(Fore.YELLOW + "Plan cancelado.")
                        continue

                    print(Fore.WHITE + "\nEjecutando plan...\n")
                    resultado = MODULOS["orquestador"].ejecutar_plan(pasos, MODULOS)
                    print(Fore.GREEN + "\nMECANICO - RESUMEN FINAL:\n")
                    print(Fore.WHITE + resultado)

                except Exception as e:
                    guardar_error(str(e), "Modo auto orquestador")
                    print(Fore.RED + f"\nError en orquestador: {e}")

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
                    for api, resp in resultados.items():
                        print(Fore.CYAN + f"\n[{api.upper()}]:")
                        print(Fore.WHITE + resp)
                except Exception as e:
                    guardar_error(str(e), "Modo consenso")

        elif opcion == "4":
            ver_apis()

    except KeyboardInterrupt:
        print(Fore.CYAN + "\nHasta luego.")
        break
    except Exception as e:
        guardar_error(str(e), "Loop principal")
        print(Fore.RED + "\nError capturado. MECANICO sigue funcionando.")
        continue

```

### 📂 Archivo: `memoria\token_log.json`
```json
{
  "groq": {
    "dias": {
      "2026-06-29": {
        "input": 3499,
        "output": 2955
      },
      "2026-06-30": {
        "input": 2893,
        "output": 1606
      },
      "2026-07-01": {
        "input": 2314,
        "output": 2869
      },
      "2026-07-09": {
        "input": 25506,
        "output": 23840
      }
    },
    "horas": {
      "2026-06-29 07:00": {
        "input": 93,
        "output": 61
      },
      "2026-06-29 14:00": {
        "input": 93,
        "output": 73
      },
      "2026-06-29 15:00": {
        "input": 3313,
        "output": 2821
      },
      "2026-06-30 05:00": {
        "input": 2893,
        "output": 1606
      },
      "2026-07-01 02:00": {
        "input": 2111,
        "output": 2508
      },
      "2026-07-01 03:00": {
        "input": 93,
        "output": 55
      },
      "2026-07-01 16:00": {
        "input": 110,
        "output": 306
      },
      "2026-07-09 00:00": {
        "input": 794,
        "output": 1717
      },
      "2026-07-09 20:00": {
        "input": 16111,
        "output": 13639
      },
      "2026-07-09 21:00": {
        "input": 4749,
        "output": 4788
      },
      "2026-07-09 22:00": {
        "input": 3852,
        "output": 3696
      }
    }
  },
  "nvidia": {
    "dias": {
      "2026-06-29": {
        "input": 91,
        "output": 318
      }
    },
    "horas": {
      "2026-06-29 15:00": {
        "input": 91,
        "output": 318
      }
    }
  },
  "cerebras": {
    "dias": {
      "2026-06-29": {
        "input": 120,
        "output": 270
      }
    },
    "horas": {
      "2026-06-29 15:00": {
        "input": 120,
        "output": 270
      }
    }
  },
  "ollama": {
    "dias": {
      "2026-07-09": {
        "input": 1300,
        "output": 1123
      }
    },
    "horas": {
      "2026-07-09 01:00": {
        "input": 236,
        "output": 233
      },
      "2026-07-09 03:00": {
        "input": 236,
        "output": 201
      },
      "2026-07-09 20:00": {
        "input": 828,
        "output": 689
      }
    }
  },
  "gemini": {
    "dias": {
      "2026-07-09": {
        "input": 1568,
        "output": 1292
      }
    },
    "horas": {
      "2026-07-09 01:00": {
        "input": 308,
        "output": 300
      },
      "2026-07-09 03:00": {
        "input": 304,
        "output": 284
      },
      "2026-07-09 20:00": {
        "input": 956,
        "output": 708
      }
    }
  }
}
```

### 📂 Archivo: `modulos\analizador.py`
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
    for raiz, dirs, archivos in os.walk(carpeta):
        dirs[:] = [d for d in dirs if d not in ["__pycache__", ".git", "node_modules"]]
        for archivo in archivos:
            if archivo.endswith(".py"):
                ruta = os.path.join(raiz, archivo)
                total_archivos += 1
                analisis = analizar_python(ruta)
                if "Errores: 0" not in analisis and not analisis.startswith("ERROR"):
                    total_errores += 1
                    reporte.append(analisis)
    resumen = f"ANÁLISIS DE PROYECTO: {carpeta}\n"
    resumen += f"Archivos Python analizados: {total_archivos}\n"
    resumen += f"Archivos con errores: {total_errores}\n"
    resumen += "=" * 40 + "\n"
    if reporte:
        resumen += "\n".join(reporte)
    else:
        resumen += "No se encontraron errores de sintaxis."
    return resumen

def analizar_con_ia(ruta: str, preguntar_fn) -> str:
    """Analiza un archivo con la ayuda de la inteligencia artificial."""
    codigo = leer_archivo(ruta)
    if codigo.startswith("ERROR"):
        return codigo
    prompt = f"""Analizá este código y encontrá:
1. Errores o bugs
2. Problemas de rendimiento
3. Mejoras posibles
4. Código duplicado

Archivo: {ruta}
Código:
{codigo[:3000]}

Respondé en español, sé conciso y directo."""
    return preguntar_fn(prompt)

def ejecutar(accion: str, texto: str) -> str:
    """Ejecuta la acción solicitada."""
    t = texto.lower()
    palabras = texto.split()

    if "proyecto" in t:
        carpeta = palabras[-1] if len(palabras) > 1 else BASE
        return analizar_proyecto(carpeta)
    elif "ia" in t or "inteligente" in t:
        ruta = palabras[-1] if len(palabras) > 1 else ""
        if not ruta or not os.path.exists(ruta):
            return "ERROR: Especifica la ruta del archivo. Ej: analizar ia C:/ruta/archivo.py"
        from mecanico import preguntar
        return analizar_con_ia(ruta, preguntar)
    elif "archivo" in t:
        ruta = palabras[-1] if len(palabras) > 1 else ""
        if not ruta or not os.path.exists(ruta):
            return "ERROR: Especifica la ruta del archivo. Ej: analizar archivo C:/ruta/archivo.py"
        return analizar_python(ruta)
    else:
        return "ERROR: Acción no reconocida. Opciones: proyecto, ia, archivo"

# Uso ejemplo
if __name__ == "__main__":
    print(ejecutar("accion", "analizar proyecto C:/IA/AGENTE/MECANICO"))
    print(ejecutar("accion", "analizar ia C:/rito/archivo.py"))
    print(ejecutar("accion", "analizar archivo C:/rito/archivo.py"))
```

### 📂 Archivo: `modulos\autoeditor.py`
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
    """Agrega el trigger al mecanico.py automaticamente"""
    try:
        with open(MECANICO_PY, "r", encoding="utf-8") as f:
            contenido = f.read()

        # Verificar si el trigger ya existe
        if f"entrada.lower().startswith(\"{trigger}\")" in contenido:
            return f"INFO: Trigger '{trigger}' ya existe en mecanico.py"

        # Bloque del trigger a insertar
        bloque = (
            f"\n                if entrada.lower().startswith(\"{trigger}\"):\n"
            f"                    if \"{nombre_modulo}\" in MODULOS:\n"
            f"                        resultado = MODULOS[\"{nombre_modulo}\"].ejecutar(\"{trigger}\", entrada)\n"
            f"                        print(Fore.GREEN + f\"\\nMECANICO: {{resultado}}\")\n"
            f"                    continue\n"
        )

        # Insertar antes del bloque de respuesta con IA
        marca = "                try:\n                    print(Fore.WHITE + \"Pensando...\""
        if marca not in contenido:
            return "ERROR: No se encontro el punto de insercion en mecanico.py"

        contenido_nuevo = contenido.replace(marca, bloque + marca, 1)

        hacer_backup("mecanico.py")
        with open(MECANICO_PY, "w", encoding="utf-8") as f:
            f.write(contenido_nuevo)

        return f"OK Trigger '{trigger}' agregado a mecanico.py"

    except Exception as e:
        return f"ERROR agregando trigger: {e}"

def ejecutar_instruccion(json_str):
    try:
        instruccion = json.loads(json_str)
    except json.JSONDecodeError as e:
        return f"ERROR: JSON invalido: {e}"

    log = []
    accion = instruccion.get("accion")
    archivo = instruccion.get("archivo", "")
    contenido = instruccion.get("contenido", "")
    backup = instruccion.get("backup", True)
    descripcion = instruccion.get("descripcion", "")
    trigger = instruccion.get("trigger", "")

    if backup and archivo:
        b = hacer_backup(archivo)
        if b:
            log.append(b)

    if accion in ["crear_modulo", "crear_archivo"]:
        if archivo.endswith(".py"):
            valido, msg = validar_python(contenido)
            log.append(msg)
            if not valido:
                return "\n".join(log)
        resultado = escribir_archivo(archivo, contenido)
        log.append(resultado)

        # Agregar trigger automaticamente si se especifica
        if trigger and archivo.startswith("modulos/"):
            nombre_modulo = os.path.basename(archivo).replace(".py", "")
            resultado_trigger = agregar_trigger(trigger, nombre_modulo)
            log.append(resultado_trigger)

    elif accion == "leer_archivo":
        contenido_leido = leer_archivo(archivo)
        if contenido_leido:
            return f"Contenido de {archivo}:\n{contenido_leido}"
        return f"ERROR: No encontrado: {archivo}"

    elif accion == "modificar_con_ia":
        contenido_actual = leer_archivo(archivo)
        if not contenido_actual:
            return f"ERROR: Archivo no encontrado: {archivo}"
        try:
            from mecanico import preguntar
            prompt = (
                "Sos un experto en Python. Modificá este archivo segun la instruccion.\n"
                f"Instruccion: {descripcion}\n"
                "Devolvé SOLO el codigo Python completo y modificado entre triple backticks.\n"
                "No agregues explicaciones.\n\n"
                f"Archivo actual:\n```python\n{contenido_actual}\n```\n\n"
                "Devolvé SOLO el codigo modificado:"
            )
            respuesta = preguntar(prompt)
            codigo_nuevo = extraer_codigo(respuesta)
            if not codigo_nuevo:
                return "ERROR: La IA no devolvio codigo"
            if archivo.endswith(".py"):
                valido, msg = validar_python(codigo_nuevo)
                if not valido:
                    return f"ERROR: Codigo invalido: {msg}"
                log.append("Codigo valido")
            resultado = escribir_archivo(archivo, codigo_nuevo)
            log.append(resultado)
        except Exception as e:
            return f"ERROR: {e}"

    elif accion == "agregar_trigger":
        nombre_modulo = instruccion.get("modulo", "")
        if not trigger or not nombre_modulo:
            return "ERROR: Se necesita trigger y modulo"
        resultado = agregar_trigger(trigger, nombre_modulo)
        log.append(resultado)

    log.append("OK Instruccion ejecutada correctamente")
    return "\n".join(log)

def ejecutar(accion, texto):
    inicio = texto.find("{")
    fin = texto.rfind("}") + 1
    if inicio == -1 or fin == 0:
        return "ERROR: No encontre un JSON valido"
    return ejecutar_instruccion(texto[inicio:fin])

```

### 📂 Archivo: `modulos\bucle_mejora.py`
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
    log.append("El archivo quedo mejorado pero podria tener detalles pendientes. Revisalo o segui iterando manualmente.")
    return "\n".join(log)

def ejecutar(accion, texto):
    palabras = texto.split()
    ruta = None
    for p in palabras:
        if os.path.exists(p) and p.endswith(".py"):
            ruta = p
            break
    if not ruta:
        return "ERROR: Especifica la ruta completa del archivo .py. Ej: bucle mejora C:/ruta/archivo.py"
    from mecanico import preguntar
    import mecanico
    return bucle_mejorar_archivo(ruta, preguntar, mecanico.MODULOS)

```

### 📂 Archivo: `modulos\buscador_web.py`
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
        query = " ".join(palabras[1:])
        return obtener_contexto(query)
    else:
        for kw in ["buscar web", "buscar internet", "buscar en internet", "investigar"]:
            texto = texto.replace(kw, "", 1) if kw in texto.lower() else texto
        query = texto.strip()
        if not query:
            return "ERROR: Especifica que buscar. Ej: buscar web python 3.13 novedades"
        return buscar(query)

```

### 📂 Archivo: `modulos\explorador.py`
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
        return f"ERROR: {e}"

def mover(origen, destino):
    try:
        shutil.move(origen, destino)
        return f"OK Movido: {origen} -> {destino}"
    except Exception as e:
        return f"ERROR: {e}"

def leer(ruta):
    if not os.path.exists(ruta):
        return f"ERROR: Archivo no encontrado: {ruta}"
    if os.path.isdir(ruta):
        return f"ERROR: {ruta} es una carpeta, usa 'explorar listar' en vez de leer"
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
        lineas = contenido.split("\n")
        if len(lineas) > 50:
            return f"Primeras 50 lineas de {ruta}:\n" + "\n".join(lineas[:50]) + f"\n...({len(lineas)} lineas total)"
        return f"Contenido de {ruta}:\n{contenido}"
    except Exception as e:
        return f"ERROR: {e}"

def info(ruta):
    if not os.path.exists(ruta):
        return f"ERROR: Ruta no encontrada: {ruta}"
    stat = os.stat(ruta)
    modificado = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    size = stat.st_size
    size_str = f"{size} bytes" if size < 1024 else f"{round(size/1024/1024, 2)} MB"
    tipo = "Carpeta" if os.path.isdir(ruta) else "Archivo"
    return f"Info de {ruta}:\nTipo: {tipo}\nTamanio: {size_str}\nModificado: {modificado}"

def ejecutar(accion, texto):
    palabras = texto.split()
    t = texto.lower()

    if "listar" in t or "ver carpeta" in t:
        ruta = palabras[-1] if len(palabras) > 1 else "C:/"
        return listar(ruta)
    elif "buscar" in t:
        if len(palabras) >= 3:
            return buscar(palabras[-1], palabras[-2])
        return "ERROR: Uso: explorar buscar patron C:/ruta"
    elif "crear carpeta" in t:
        ruta = palabras[-1]
        return crear_carpeta(ruta)
    elif "copiar" in t:
        if len(palabras) >= 3:
            return copiar(palabras[-2], palabras[-1])
        return "ERROR: Uso: explorar copiar origen destino"
    elif "mover" in t:
        if len(palabras) >= 3:
            return mover(palabras[-2], palabras[-1])
        return "ERROR: Uso: explorar mover origen destino"
    elif "leer" in t:
        ruta = palabras[-1]
        return leer(ruta)
    elif "info" in t:
        ruta = palabras[-1]
        return info(ruta)
    else:
        ruta = palabras[-1] if len(palabras) > 1 else "C:/"
        return listar(ruta)

```

### 📂 Archivo: `modulos\generador.py`
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
            valido, msg = validar_python(codigo)
            if not valido:
                log.append(f"  {api}: codigo invalido - {msg}")
                continue
            if "def ejecutar(" not in codigo:
                log.append(f"  {api}: falta funcion ejecutar")
                continue
            codigo_nuevo = codigo
            api_usada = api
            break
        except Exception as e:
            log.append(f"  {api}: error - {e}")
            continue
    if not codigo_nuevo:
        return "\n".join(log) + "\nERROR: Ninguna API pudo generar el modulo"
    nombre_archivo = nombre.lower().replace(" ", "_").replace("-", "_")
    if not nombre_archivo.endswith(".py"):
        nombre_archivo += ".py"
    ruta = os.path.join(BASE, "modulos", nombre_archivo)
    if os.path.exists(ruta):
        return f"ERROR: El modulo {nombre_archivo} ya existe. Usa otro nombre."
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(codigo_nuevo)
    log.append(f"Codigo valido generado por {api_usada}")
    log.append(f"Modulo guardado: {ruta}")
    log.append(f"Lineas: {len(codigo_nuevo.splitlines())}")

    nombre_trigger = nombre_archivo[:-3] if nombre_archivo.endswith(".py") else nombre_archivo
    try:
        from modulos import autoeditor
        resultado_trigger = autoeditor.agregar_trigger(nombre_trigger, nombre_trigger)
        log.append(resultado_trigger)
    except Exception as e:
        log.append(f"No se pudo agregar trigger automatico: {e}")

    log.append("OK Modulo generado exitosamente")
    log.append(f"Escribi 'recargar' para cargar el modulo {nombre_archivo}")
    return "\n".join(log)
def ejecutar(accion, texto):
    if "::" not in texto:
        return "ERROR: Uso: generar descripcion del modulo :: nombre_modulo"
    partes = texto.split("::", 1)
    descripcion = partes[0].replace("generar ", "").strip()
    nombre = partes[1].strip()
    from mecanico import preguntar
    return generar_modulo(descripcion, nombre, preguntar)

```

### 📂 Archivo: `modulos\git_manager.py`
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
        return ver_historial()
    else:
        return commit_automatico()

```

### 📂 Archivo: `modulos\github_reader.py`
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

```

### 📂 Archivo: `modulos\github_scout.py`
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
```

### 📂 Archivo: `modulos\lector_contexto.py`
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
# internamente para llamar a esta nueva función, manteniendo su interfaz externa.
def leer_archivo_y_realizar_pregunta(
    ruta: str,
    pregunta: str,
    preguntar_fn: Callable[[str], str],
    max_lineas_contexto: int = 200
) -> str:
    """
    Lee el contenido de un archivo (con un límite configurable de líneas) y formula una pregunta
    basada en su contenido, utilizando una función de consulta proporcionada.

    Esta función mejora la robustez mediante validaciones de parámetros, manejo de errores
    más detallado y lectura eficiente de archivos.

    Args:
        ruta (str): La ruta del archivo a leer. Debe ser una cadena no vacía y apuntar a un archivo existente.
        pregunta (str): La pregunta que se desea formular sobre el contenido del archivo.
                        Debe ser una cadena no vacía.
        preguntar_fn (Callable[[str], str]): Una función callable (ej. un modelo de lenguaje)
                                             que toma un string (el prompt) y devuelve un string (la respuesta).
                                             Este parámetro es obligatorio y no puede ser None.
        max_lineas_contexto (int): El número máximo de líneas del archivo a incluir en el contexto
                                   enviado a `preguntar_fn`. Esto ayuda a gestionar el tamaño de entrada
                                   para modelos de lenguaje. Por defecto es 200 líneas.

    Returns:
        str: La respuesta generada por `preguntar_fn` basada en el prompt,
             o un mensaje de error descriptivo si ocurre algún problema durante el proceso
             (ej. archivo no encontrado, errores de lectura, parámetros inválidos).
    """
    # 1. Validación de parámetros y 2. Manejo de errores (TypeError)
    # Se verifica que los parámetros `ruta` y `pregunta` sean cadenas válidas y no estén vacías.
    if not isinstance(ruta, str) or not ruta.strip():
        logger.error(f"Error de validación: El parámetro 'ruta' es inválido o vacío: '{ruta}'")
        return "ERROR: La ruta del archivo no puede ser vacía o inválida."
    if not isinstance(pregunta, str) or not pregunta.strip():
        logger.error(f"Error de validación: El parámetro 'pregunta' es inválido o vacío: '{pregunta}'")
        return "ERROR: La pregunta no puede ser vacía o inválida."
    # 11. Comprobación de `None`: Se confía en el tipado (`Callable`) y en que Python lanzará un TypeError
    # si se intenta llamar a un objeto que no es callable (incluyendo `None`) en tiempo de ejecución.

    # 10. Tipado: Se han añadido los tipos a los parámetros y el valor de retorno.
    # 9. Nombres de variables: `ruta_path` es más descriptivo.
    ruta_path = Path(ruta)

    # 8. Comprobación de ruta: Se usa `is_file()` para asegurar que la ruta es un archivo, no un directorio.
    if not ruta_path.is_file():
        logger.error(f"Error de archivo: La ruta '{ruta_path}' no es un archivo válido o no existe.")
        return f"ERROR: Archivo no encontrado o no es un archivo válido: {ruta_path}"

    contenido_lineas: list[str] = []
    lineas_totales = 0
    try:
        # 3. Lectura de archivo: Se lee el archivo línea por línea para optimizar la memoria
        # con archivos grandes, en lugar de leer todo el contenido de una vez.
        # 4. Codificación: Se mantiene `errors="replace"` y se añade manejo específico de `UnicodeDecodeError`.
        with ruta_path.open("r", encoding="utf-8", errors="replace") as f:
            for i, linea in enumerate(f):
                # 5. Límite de líneas: El límite es configurable mediante `max_lineas_contexto`.
                if i < max_lineas_contexto:
                    contenido_lineas.append(linea.rstrip('\n'))  # Elimina el salto de línea para procesamiento consistente
                lineas_totales += 1
    except FileNotFoundError:
        # Aunque `is_file()` ya debería haberlo capturado, es una buena práctica por si acaso.
        logger.exception(f"Error inesperado: Archivo no encontrado para la ruta '{ruta_path}' durante la lectura.")
        return f"ERROR: Archivo no encontrado: {ruta_path}"
    except PermissionError as e:
        logger.exception(f"Error de permisos al leer el archivo '{ruta_path}': {e}")
        return f"ERROR: Permiso denegado para leer el archivo: {ruta_path}"
    except OSError as e:
        logger.exception(f"Error del sistema operativo al leer el archivo '{ruta_path}': {e}")
        return f"ERROR: Error del sistema operativo al leer el archivo: {e}"
    except UnicodeDecodeError as e:
        # Esto debería ser mitigado por `errors="replace"`, pero un catch explícito es útil.
        logger.exception(f"Error de codificación al leer el archivo '{ruta_path}': {e}")
        return f"ERROR: Error de codificación al leer el archivo (se utilizó 'replace'): {e}"
    except Exception as e:
        logger.exception(f"Ocurrió un error inesperado al leer el archivo '{ruta_path}': {e}")
        return f"ERROR: Error inesperado al leer el archivo: {e}"

    contenido_recortado = "\n".join(contenido_lineas)
    if lineas_totales > max_lineas_contexto:
        contenido_recortado += (f"\n...({lineas_totales} líneas totales, "
                                f"mostrando las primeras {max_lineas_contexto})")

    prompt = f"""Analiza este archivo y responde en español.
Archivo: {ruta_path}
Pregunta: {pregunta}

Contenido:
{contenido_recortado}

Responde directamente a la pregunta basándote en el contenido real del archivo."""

    logger.debug(f"Prompt generado para 'preguntar_fn':\n{prompt}")
    try:
        return preguntar_fn(prompt)
    except Exception as e:
        logger.exception(f"Error al ejecutar la función 'preguntar_fn' con el prompt.")
        return f"ERROR: Fallo al procesar la pregunta: {e}"


# CRITICO: La función `ejecutar` DEBE mantenerse exactamente igual en su nombre y firma.
# 6. Organización del código: Su implementación interna se ha mejorado para usar la función
# `leer_archivo_y_realizar_pregunta` y para ser más robusta.
def ejecutar(accion: str, texto: str) -> str:
    """
    Ejecuta la acción de leer y preguntar sobre un archivo.
    Este es el punto de entrada principal para acciones relacionadas con la lectura de contexto.
    Parsea el texto de entrada para extraer la ruta del archivo y la pregunta,
    y luego utiliza la funcionalidad de lectura de archivo y pregunta.

    Args:
        accion (str): La acción a realizar. Se espera que sea "leer". Este parámetro
                      se usa para el logging pero no para la lógica principal.
        texto (str): El texto de entrada que contiene la ruta del archivo y la pregunta,
                     siguiendo el formato "leer C:/ruta/archivo.js y qué hace este código".

    Returns:
        str: La respuesta a la pregunta obtenida del procesador de lenguaje (via `preguntar_fn`),
             o un mensaje de error si la entrada es inválida o el procesamiento falla.
    """
    logger.info(f"Ejecutando la acción '{accion}' con el texto: '{texto}'")

    # Se mantiene la lógica de parsing original para preservar la funcionalidad exacta.
    partes = texto.split(" y ", 1)
    if len(partes) < 2:
        partes = texto.split(" para ", 1)
    if len(partes) < 2:
        logger.warning(f"Formato de entrada incorrecto para 'ejecutar'. Texto recibido: '{texto}'")
        return "ERROR: Uso: leer C:/ruta/archivo.js y qué hace este código"

    ruta_parte = partes[0].replace("leer ", "").strip()
    # 9. Nombres de variables: `pregunta_texto` es más descriptivo para evitar conflictos.
    pregunta_texto = partes[1].strip()

    # Se verifica si la función `preguntar` fue importada exitosamente al inicio del script.
    if preguntar is None:
        logger.error("La función 'preguntar' de 'mecanico' no está disponible. No se puede proceder.")
        return "ERROR: La funcionalidad de pregunta no está disponible (módulo 'mecanico' no cargado o falló)."

    # Se llama a la función de lectura y pregunta mejorada, pasando `preguntar` como callable.
    return leer_archivo_y_realizar_pregunta(ruta_parte, pregunta_texto, preguntar)
```

### 📂 Archivo: `modulos\memoria_historial.py`
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
        logging.error(f"Error al ejecutar accion: {e}")
        return f"Error al ejecutar accion: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    print(ejecutar("registrar", "cambio de aceite"))
    print(ejecutar("ver", ""))
```

### 📂 Archivo: `modulos\Nueva carpeta\asfasf.py`
```python
import os
import json
import shutil
import datetime
import ast

BASE = "C:/IA/AGENTE/MECANICO"

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
    except Exception as e:
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

def ejecutar_instruccion(json_str):
    try:
        instruccion = json.loads(json_str)
    except json.JSONDecodeError as e:
        return f"ERROR: JSON invalido: {e}"

    log = []
    accion = instruccion.get("accion")
    archivo = instruccion.get("archivo", "")
    contenido = instruccion.get("contenido", "")
    backup = instruccion.get("backup", True)
    descripcion = instruccion.get("descripcion", "")

    if backup and archivo:
        b = hacer_backup(archivo)
        if b:
            log.append(b)

    if accion in ["crear_modulo", "crear_archivo"]:
        if archivo.endswith(".py"):
            valido, msg = validar_python(contenido)
            log.append(msg)
            if not valido:
                return "\n".join(log)
        resultado = escribir_archivo(archivo, contenido)
        log.append(resultado)

    elif accion == "leer_archivo":
        contenido_leido = leer_archivo(archivo)
        if contenido_leido:
            return f"Contenido de {archivo}:\n{contenido_leido}"
        return f"ERROR: No encontrado: {archivo}"

    elif accion == "modificar_con_ia":
        contenido_actual = leer_archivo(archivo)
        if not contenido_actual:
            return f"ERROR: Archivo no encontrado: {archivo}"
        try:
            from mecanico import preguntar
            prompt = (
                "Sos un experto en Python. Modifica este archivo segun la instruccion.\n"
                f"Instruccion: {descripcion}\n"
                "Devolvé SOLO el codigo Python completo y modificado entre triple backticks.\n"
                "No agregues explicaciones.\n\n"
                f"Archivo actual:\n```python\n{contenido_actual}\n```\n\n"
                "Devolvé SOLO el codigo modificado:"
            )
            respuesta = preguntar(prompt)
            codigo_nuevo = extraer_codigo(respuesta)
            if not codigo_nuevo:
                return "ERROR: La IA no devolvio codigo"
            if archivo.endswith(".py"):
                valido, msg = validar_python(codigo_nuevo)
                if not valido:
                    return f"ERROR: Codigo invalido: {msg}"
                log.append("Codigo valido")
            resultado = escribir_archivo(archivo, codigo_nuevo)
            log.append(resultado)
        except Exception as e:
            return f"ERROR: {e}"

    log.append("OK Instruccion ejecutada correctamente")
    return "\n".join(log)

def ejecutar(accion, texto):
    inicio = texto.find("{")
    fin = texto.rfind("}") + 1
    if inicio == -1 or fin == 0:
        return "ERROR: No encontre un JSON valido"
    return ejecutar_instruccion(texto[inicio:fin])

```

### 📂 Archivo: `modulos\Nueva carpeta\generador.py`
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
            valido, msg = validar_python(codigo)
            if not valido:
                log.append(f"  {api}: codigo invalido - {msg}")
                continue
            if "def ejecutar(" not in codigo:
                log.append(f"  {api}: falta funcion ejecutar")
                continue
            codigo_nuevo = codigo
            api_usada = api
            break
        except Exception as e:
            log.append(f"  {api}: error - {e}")
            continue
    if not codigo_nuevo:
        return "\n".join(log) + "\nERROR: Ninguna API pudo generar el modulo"
    nombre_archivo = nombre.lower().replace(" ", "_").replace("-", "_")
    if not nombre_archivo.endswith(".py"):
        nombre_archivo += ".py"
    ruta = os.path.join(BASE, "modulos", nombre_archivo)
    if os.path.exists(ruta):
        return f"ERROR: El modulo {nombre_archivo} ya existe. Usa otro nombre."
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(codigo_nuevo)
    log.append(f"Codigo valido generado por {api_usada}")
    log.append(f"Modulo guardado: {ruta}")
    log.append(f"Lineas: {len(codigo_nuevo.splitlines())}")
    log.append("OK Modulo generado exitosamente")
    log.append(f"Reinicia MECANICO para cargar el modulo {nombre_archivo}")
    return "\n".join(log)

def ejecutar(accion, texto):
    partes = texto.split(" como ", 1)
    if len(partes) < 2:
        partes = texto.split(" llamado ", 1)
    if len(partes) < 2:
        return "ERROR: Uso: generar modulo que hace X como nombre_modulo"
    descripcion = partes[0].replace("generar ", "").strip()
    nombre = partes[1].strip()
    from mecanico import preguntar
    return generar_modulo(descripcion, nombre, preguntar)

```

### 📂 Archivo: `modulos\Nueva carpeta\mecanico (1).py`
```python
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
        return
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".py") and not archivo.startswith("_"):
            nombre = archivo.replace(".py", "")
            try:
                mod = importlib.import_module(f"modulos.{nombre}")
                MODULOS[nombre] = mod
                print(Fore.GREEN + f"  OK {nombre}")
            except Exception as e:
                print(Fore.RED + f"  ERROR {nombre}: {e}")

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
                    pass
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
    print(Fore.CYAN + "   MECANICO IA - Agente Reparador")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "  1. Modo Manual    - vos le decis que hacer")
    print(Fore.WHITE + "  2. Modo Auto      - MECANICO trabaja solo")
    print(Fore.WHITE + "  3. Modo Consenso  - todas las APIs juntas")
    print(Fore.WHITE + "  4. Ver APIs       - estado de las APIs")
    print(Fore.WHITE + "  5. Cambiar API    - elegir con que IA trabajar")
    print(Fore.WHITE + "  s. Salir")
    print(Fore.CYAN + "=" * 55)

def mostrar_menu_apis():
    from config import APIS
    print()
    print(Fore.CYAN + "=" * 55)
    print(Fore.CYAN + "   Elegir API activa")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "  0. Auto (groq > gemini > cerebras > zai > ollama)")
    apis = list(APIS.items())
    for i, (nombre, config) in enumerate(apis, 1):
        tiene_key = bool(config["key"]) or nombre == "ollama"
        estado = Fore.GREEN + "OK" if (config["activa"] and tiene_key) else Fore.RED + "OFF"
        print(f"  {i}. {estado} {nombre:<12} {config['modelo']}")
    print(Fore.CYAN + "=" * 55)
    return apis

def elegir_api():
    apis = mostrar_menu_apis()
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
    from config import APIS
    print()
    print(Fore.CYAN + "Estado de APIs:")
    for nombre, config in APIS.items():
        tiene_key = bool(config["key"]) or nombre == "ollama"
        estado = Fore.GREEN + "OK" if (config["activa"] and tiene_key) else Fore.RED + "INACTIVA"
        print(f"  {estado} {nombre:<12} modelo: {config['modelo']}")
    print()

def hacer_prompt(entrada, api_actual):
    return (
        "Sos MECANICO, un agente IA especializado en analizar, reparar y mejorar codigo.\n"
        "Siempre respondes en espanol. Sos directo y tecnico.\n"
        f"Fecha actual: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
        f"Usuario: {entrada}"
    )

print()
print(Fore.CYAN + "=" * 55)
print(Fore.CYAN + "   MECANICO IA arrancando...")
print(Fore.CYAN + "=" * 55)
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
        opcion = input(Fore.YELLOW + "Elegi 1, 2, 3, 4, 5 o s: ").strip().lower()

        if opcion == "s":
            print(Fore.CYAN + "Hasta luego.")
            break

        elif opcion == "5":
            api_actual = elegir_api()

        elif opcion == "1":
            print(Fore.GREEN + f"\nModo Manual activado. API: {api_actual}")
            print(Fore.WHITE + "Comandos: 'api' cambiar API | 'recargar' nuevos modulos | 'menu' volver | 'salir' terminar")
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
                if entrada.lower() == "recargar":
                    resultado = recargar_modulos()
                    print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("ejecutar json"):
                    if "autoeditor" in MODULOS:
                        resultado = MODULOS["autoeditor"].ejecutar("autoeditar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("generar"):
                    if "generador" in MODULOS:
                        resultado = MODULOS["generador"].ejecutar("generar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("github") or entrada.lower().startswith("scout"):
                    if "github_scout" in MODULOS:
                        resultado = MODULOS["github_scout"].ejecutar("scout", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("mejorar"):
                    if "reparador" in MODULOS:
                        resultado = MODULOS["reparador"].ejecutar("mejorar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("reparar"):
                    if "reparador" in MODULOS:
                        resultado = MODULOS["reparador"].ejecutar("reparar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("revertir"):
                    if "revertir" in MODULOS:
                        resultado = MODULOS["revertir"].ejecutar("revertir", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("analizar"):
                    if "analizador" in MODULOS:
                        resultado = MODULOS["analizador"].ejecutar("analizar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("leer"):
                    if "lector_contexto" in MODULOS:
                        resultado = MODULOS["lector_contexto"].ejecutar("leer", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("explorar"):
                    if "explorador" in MODULOS:
                        resultado = MODULOS["explorador"].ejecutar("explorar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("git"):
                    if "git_manager" in MODULOS:
                        resultado = MODULOS["git_manager"].ejecutar("git", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                try:
                    print(Fore.WHITE + "Pensando...", end="", flush=True)
                    inicio = time.time()
                    respuesta = preguntar(hacer_prompt(entrada, api_actual), api=api_actual)
                    fin = round(time.time() - inicio, 2)
                    print(Fore.GREEN + f"\rMECANICO [{api_actual}] ({fin}s): " + Fore.WHITE + respuesta)
                except Exception as e:
                    guardar_error(str(e), "Modo manual")

        elif opcion == "2":
            print(Fore.GREEN + "\nModo Auto activado. (En construccion)")

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
                    for api, resp in resultados.items():
                        print(Fore.CYAN + f"\n[{api.upper()}]:")
                        print(Fore.WHITE + resp)
                except Exception as e:
                    guardar_error(str(e), "Modo consenso")

        elif opcion == "4":
            ver_apis()

    except KeyboardInterrupt:
        print(Fore.CYAN + "\nHasta luego.")
        break
    except Exception as e:
        guardar_error(str(e), "Loop principal")
        print(Fore.RED + "\nError capturado. MECANICO sigue funcionando.")
        continue

```

### 📂 Archivo: `modulos\Nueva carpeta\mecanico.py`
```python
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
        return
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".py") and not archivo.startswith("_"):
            nombre = archivo.replace(".py", "")
            try:
                mod = importlib.import_module(f"modulos.{nombre}")
                MODULOS[nombre] = mod
                print(Fore.GREEN + f"  OK {nombre}")
            except Exception as e:
                print(Fore.RED + f"  ERROR {nombre}: {e}")

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
                    pass
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
    print(Fore.CYAN + "   MECANICO IA - Agente Reparador")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "  1. Modo Manual    - vos le decis que hacer")
    print(Fore.WHITE + "  2. Modo Auto      - MECANICO trabaja solo")
    print(Fore.WHITE + "  3. Modo Consenso  - todas las APIs juntas")
    print(Fore.WHITE + "  4. Ver APIs       - estado de las APIs")
    print(Fore.WHITE + "  5. Cambiar API    - elegir con que IA trabajar")
    print(Fore.WHITE + "  s. Salir")
    print(Fore.CYAN + "=" * 55)

def mostrar_menu_apis():
    from config import APIS
    print()
    print(Fore.CYAN + "=" * 55)
    print(Fore.CYAN + "   Elegir API activa")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "  0. Auto (groq > gemini > cerebras > zai > ollama)")
    apis = list(APIS.items())
    for i, (nombre, config) in enumerate(apis, 1):
        tiene_key = bool(config["key"]) or nombre == "ollama"
        estado = Fore.GREEN + "OK" if (config["activa"] and tiene_key) else Fore.RED + "OFF"
        print(f"  {i}. {estado} {nombre:<12} {config['modelo']}")
    print(Fore.CYAN + "=" * 55)
    return apis

def elegir_api():
    apis = mostrar_menu_apis()
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
    from config import APIS
    print()
    print(Fore.CYAN + "Estado de APIs:")
    for nombre, config in APIS.items():
        tiene_key = bool(config["key"]) or nombre == "ollama"
        estado = Fore.GREEN + "OK" if (config["activa"] and tiene_key) else Fore.RED + "INACTIVA"
        print(f"  {estado} {nombre:<12} modelo: {config['modelo']}")
    print()

def hacer_prompt(entrada, api_actual):
    return (
        "Sos MECANICO, un agente IA especializado en analizar, reparar y mejorar codigo.\n"
        "Siempre respondes en espanol. Sos directo y tecnico.\n"
        f"Fecha actual: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
        f"Usuario: {entrada}"
    )

print()
print(Fore.CYAN + "=" * 55)
print(Fore.CYAN + "   MECANICO IA arrancando...")
print(Fore.CYAN + "=" * 55)
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
        opcion = input(Fore.YELLOW + "Elegi 1, 2, 3, 4, 5 o s: ").strip().lower()

        if opcion == "s":
            print(Fore.CYAN + "Hasta luego.")
            break

        elif opcion == "5":
            api_actual = elegir_api()

        elif opcion == "1":
            print(Fore.GREEN + f"\nModo Manual activado. API: {api_actual}")
            print(Fore.WHITE + "Comandos: 'api' cambiar API | 'recargar' cargar modulos nuevos | 'menu' volver | 'salir' terminar")
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
                if entrada.lower() == "recargar":
                    resultado = recargar_modulos()
                    print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("ejecutar json"):
                    if "autoeditor" in MODULOS:
                        resultado = MODULOS["autoeditor"].ejecutar("autoeditar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("generar"):
                    if "generador" in MODULOS:
                        resultado = MODULOS["generador"].ejecutar("generar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("mejorar"):
                    if "reparador" in MODULOS:
                        resultado = MODULOS["reparador"].ejecutar("mejorar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("reparar"):
                    if "reparador" in MODULOS:
                        resultado = MODULOS["reparador"].ejecutar("reparar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("revertir"):
                    if "revertir" in MODULOS:
                        resultado = MODULOS["revertir"].ejecutar("revertir", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("analizar"):
                    if "analizador" in MODULOS:
                        resultado = MODULOS["analizador"].ejecutar("analizar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("leer"):
                    if "lector_contexto" in MODULOS:
                        resultado = MODULOS["lector_contexto"].ejecutar("leer", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("explorar"):
                    if "explorador" in MODULOS:
                        resultado = MODULOS["explorador"].ejecutar("explorar", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                if entrada.lower().startswith("git"):
                    if "git_manager" in MODULOS:
                        resultado = MODULOS["git_manager"].ejecutar("git", entrada)
                        print(Fore.GREEN + f"\nMECANICO: {resultado}")
                    continue

                try:
                    print(Fore.WHITE + "Pensando...", end="", flush=True)
                    inicio = time.time()
                    respuesta = preguntar(hacer_prompt(entrada, api_actual), api=api_actual)
                    fin = round(time.time() - inicio, 2)
                    print(Fore.GREEN + f"\rMECANICO [{api_actual}] ({fin}s): " + Fore.WHITE + respuesta)
                except Exception as e:
                    guardar_error(str(e), "Modo manual")

        elif opcion == "2":
            print(Fore.GREEN + "\nModo Auto activado. (En construccion)")

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
                    for api, resp in resultados.items():
                        print(Fore.CYAN + f"\n[{api.upper()}]:")
                        print(Fore.WHITE + resp)
                except Exception as e:
                    guardar_error(str(e), "Modo consenso")

        elif opcion == "4":
            ver_apis()

    except KeyboardInterrupt:
        print(Fore.CYAN + "\nHasta luego.")
        break
    except Exception as e:
        guardar_error(str(e), "Loop principal")
        print(Fore.RED + "\nError capturado. MECANICO sigue funcionando.")
        continue

```

### 📂 Archivo: `modulos\Nueva carpeta\token_monitor.py`
```python
import os
import json
import datetime
from dotenv import load_dotenv

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

KEYWORDS = ["tokens", "uso", "monitor tokens", "consumo", "limite"]
LOG_FILE = "C:/IA/AGENTE/MECANICO/memoria/token_log.json"

LIMITES = {
    "groq":     {"por_minuto": 12000, "por_dia": 500000},
    "gemini":   {"por_minuto": 1000000, "por_dia": 1500000},
    "cerebras": {"por_minuto": 60000, "por_dia": 1000000},
    "zai":      {"por_minuto": 10000, "por_dia": 100000},
    "ollama":   {"por_minuto": -1, "por_dia": -1}
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

def registrar_uso(api, tokens_usados):
    log = cargar_log()
    ahora = datetime.datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%Y-%m-%d %H:00")
    if api not in log:
        log[api] = {"dias": {}, "horas": {}}
    if fecha not in log[api]["dias"]:
        log[api]["dias"][fecha] = 0
    if hora not in log[api]["horas"]:
        log[api]["horas"][hora] = 0
    log[api]["dias"][fecha] += tokens_usados
    log[api]["horas"][hora] += tokens_usados
    guardar_log(log)

def ver_uso():
    log = cargar_log()
    if not log:
        return "No hay registros de uso de tokens aun.\nUsa MECANICO normalmente y los tokens se registraran automaticamente."
    ahora = datetime.datetime.now()
    hoy = ahora.strftime("%Y-%m-%d")
    hora_actual = ahora.strftime("%Y-%m-%d %H:00")
    resultado = f"USO DE TOKENS - {hoy}\n{'='*40}\n"
    for api, data in log.items():
        uso_hoy = data["dias"].get(hoy, 0)
        uso_hora = data["horas"].get(hora_actual, 0)
        limites = LIMITES.get(api, {})
        lim_dia = limites.get("por_dia", -1)
        lim_min = limites.get("por_minuto", -1)
        resultado += f"\n{api.upper()}:\n"
        resultado += f"  Hoy:        {uso_hoy:>10,} tokens"
        if lim_dia > 0:
            pct = round(uso_hoy / lim_dia * 100, 1)
            resultado += f" / {lim_dia:,} ({pct}%)"
        resultado += f"\n  Esta hora:  {uso_hora:>10,} tokens"
        if lim_min > 0:
            resultado += f" / {lim_min:,} por minuto"
        resultado += "\n"
    return resultado

def ver_historial(api=None, dias=7):
    log = cargar_log()
    if not log:
        return "No hay historial de uso"
    resultado = f"HISTORIAL ULTIMOS {dias} DIAS\n{'='*40}\n"
    ahora = datetime.datetime.now()
    for d in range(dias):
        fecha = (ahora - datetime.timedelta(days=d)).strftime("%Y-%m-%d")
        resultado += f"\n{fecha}:\n"
        apis_mostrar = [api] if api else log.keys()
        for a in apis_mostrar:
            if a in log:
                uso = log[a]["dias"].get(fecha, 0)
                if uso > 0:
                    resultado += f"  {a}: {uso:,} tokens\n"
    return resultado

def ver_limites():
    resultado = "LIMITES DE TOKENS POR API\n" + "="*40 + "\n"
    for api, limites in LIMITES.items():
        lim_min = limites["por_minuto"]
        lim_dia = limites["por_dia"]
        resultado += f"\n{api.upper()}:\n"
        resultado += f"  Por minuto: {lim_min:>10,}" if lim_min > 0 else f"  Por minuto: {'sin limite':>10}"
        resultado += f"\n  Por dia:    {lim_dia:>10,}\n" if lim_dia > 0 else f"\n  Por dia:    {'sin limite':>10}\n"
    return resultado

def ejecutar(accion, texto):
    t = texto.lower()
    if "historial" in t:
        api = None
        for a in LIMITES.keys():
            if a in t:
                api = a
                break
        return ver_historial(api)
    elif "limite" in t or "limites" in t:
        return ver_limites()
    else:
        return ver_uso()

```

### 📂 Archivo: `modulos\nvidia_selector.py`
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

```

### 📂 Archivo: `modulos\orquestador.py`
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
            contenido = data["choices"][0]["message"]["content"]
            if "<think>" in contenido and "</think>" in contenido:
                contenido = contenido.split("</think>")[-1].strip()
            return contenido, modelo
        except Exception:
            continue
    try:
        return preguntar_fn(prompt), "fallback-auto"
    except Exception:
        return None, None

def armar_plan(pedido_usuario, preguntar_fn):
    lista_modulos = "\n".join([f"- {k}: {v}" for k, v in MODULOS_DISPONIBLES.items()])
    prompt = (
        "Sos el orquestador de MECANICO, un agente que analiza y repara codigo Python.\n"
        "Tenes disponibles estos comandos exactos:\n\n"
        f"{lista_modulos}\n\n"
        "Los proyectos del usuario estan en C:/IA/AGENTE/. Si menciona un nombre de proyecto sin ruta completa,\n"
        "asumi que esta en C:/IA/AGENTE/NOMBRE_PROYECTO (ej: MAT.ONE esta en C:/IA/AGENTE/MAT.ONE).\n\n"
        f"El usuario pidio: {pedido_usuario}\n\n"
        "Arma un plan de pasos usando SOLO los comandos de arriba, con sus rutas y parametros reales.\n"
        "IMPORTANTE: si la ruta es una carpeta (no termina en .py ni otra extension), usa 'analizar proyecto <ruta>', NUNCA 'analizar <ruta>' solo para carpetas.\n"
        "Respondé SOLO con un JSON valido con este formato exacto, nada mas:\n"
        '{"pasos": ["comando1 parametro1", "comando2 parametro2"], "explicacion": "breve resumen de lo que se va a hacer"}\n\n'
        "Si no sabes exactamente que archivo reparar, SIEMPRE agrega primero explorar listar carpeta para ver los archivos disponibles, luego repara el archivo correcto.\n"
        "Para proyectos Node.js el archivo principal suele ser server.js o index.js. Para Python suele ser main.py o __init__.py.\n"
        "Si el pedido es ambiguo o falta informacion critica, pedila en el campo explicacion y deja pasos vacio.\n"
        "Responde SOLO el JSON, sin texto antes ni despues, sin backticks."
    )
    respuesta, modelo_usado = intentar_modelos_nvidia(prompt, preguntar_fn)
    if not respuesta:
        return None, "ERROR: Ninguna IA pudo armar el plan", None
    match = re.search(r'\{.*\}', respuesta, re.DOTALL)
    if not match:
        return None, f"ERROR: No se genero un plan valido.\nRespuesta: {respuesta[:300]}", None
    try:
        plan = json.loads(match.group())
        return plan.get("pasos", []), plan.get("explicacion", ""), modelo_usado
    except json.JSONDecodeError as e:
        return None, f"ERROR: JSON invalido del plan: {e}", None

def ejecutar_plan(pasos, modulos_cargados):
    resultados = []
    for i, paso in enumerate(pasos, 1):
        paso_lower = paso.lower().strip()
        resultado = None
        try:
            if paso_lower.startswith("reparar") and "reparador" in modulos_cargados:
                resultado = modulos_cargados["reparador"].ejecutar("reparar", paso)
            elif paso_lower.startswith("mejorar") and "reparador" in modulos_cargados:
                resultado = modulos_cargados["reparador"].ejecutar("mejorar", paso)
            elif paso_lower.startswith("revertir") and "revertir" in modulos_cargados:
                resultado = modulos_cargados["revertir"].ejecutar("revertir", paso)
            elif paso_lower.startswith("analizar") and "analizador" in modulos_cargados:
                resultado = modulos_cargados["analizador"].ejecutar("analizar", paso)
            elif paso_lower.startswith("explorar") and "explorador" in modulos_cargados:
                resultado = modulos_cargados["explorador"].ejecutar("explorar", paso)
            elif paso_lower.startswith("leer") and "lector_contexto" in modulos_cargados:
                resultado = modulos_cargados["lector_contexto"].ejecutar("leer", paso)
            elif paso_lower.startswith("git") and "git_manager" in modulos_cargados:
                resultado = modulos_cargados["git_manager"].ejecutar("git", paso)
            elif paso_lower.startswith("generar") and "generador" in modulos_cargados:
                resultado = modulos_cargados["generador"].ejecutar("generar", paso)
            elif paso_lower.startswith("github") and "github_reader" in modulos_cargados:
                resultado = modulos_cargados["github_reader"].ejecutar("github", paso)
            elif paso_lower.startswith("scout") and "github_scout" in modulos_cargados:
                resultado = modulos_cargados["github_scout"].ejecutar("scout", paso)
            elif paso_lower.startswith("tokens") and "token_monitor" in modulos_cargados:
                resultado = modulos_cargados["token_monitor"].ejecutar("tokens", paso)
            else:
                resultado = f"No se reconoce el comando: {paso}"
        except Exception as e:
            resultado = f"ERROR ejecutando '{paso}': {e}"
        resultados.append(f"[Paso {i}/{len(pasos)}] {paso}\n{resultado}\n")
    return "\n".join(resultados)

```

### 📂 Archivo: `modulos\reinicio.py`
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

### 📂 Archivo: `modulos\reparador.py`
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
            "```python\n" + codigo_original[:4000] + "\n```\n\n"
            "Devolvé SOLO el codigo corregido:"
        )
    else:
        log.append("Analizando para obtener sugerencias de mejora...")
        prompt_analisis = (
            "Analizá este codigo Python y listá de forma concisa las mejoras que aplicarías.\n"
            "Sé específico y técnico.\n\n"
            "```python\n" + codigo_original[:3000] + "\n```"
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
            "```python\n" + codigo_original[:3000] + "\n```\n\n"
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

```

### 📂 Archivo: `modulos\revertir.py`
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
    accion (str): Acción a realizar.
    texto (str): Texto que contiene la ruta del archivo.
    
    Retorno:
    str: Mensaje de confirmación o error.
    """
    palabras = texto.split()
    match_num = re.search(r'\d+$', texto)
    if match_num and len(palabras) > 2:
        archivo = palabras[-2]
    else:
        archivo = palabras[-1] if len(palabras) > 1 else ""
    if not archivo:
        return "ERROR: Especifica el archivo. Ej: revertir mecanico.py"
    if "listar" in texto.lower():
        return "\n".join(listar_backups(archivo))

    match = re.search(r'\d+$', texto)
    if match:
        try:
            indice = int(match.group()) - 1  # Restamos 1 para convertir a 0-index
        except ValueError:
            return "ERROR: Indice no es un numero"
    else:
        indice = 0

    return revertir(archivo, indice)

def main():
    accion = input("Ingrese la acción (listar o revertir): ")
    archivo = input("Ingrese la ruta del archivo (puede incluir el indice del backup, por ejemplo revertir mecanico.py 3): ")
    texto = f"{accion} {archivo}"
    if "listar" in texto.lower():
        try:
            print("\n".join(listar_backups(archivo)))
        except ValueError as e:
            print(e)
    elif "revertir" in texto.lower():
        try:
            resultado = revertir(archivo) if " " not in archivo else ejecutar(accion, texto)
            print(resultado)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()

```

### 📂 Archivo: `modulos\tester.py`
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

### 📂 Archivo: `modulos\texto,_creando_la_carpeta_memoria_si_no_existe_llamado_memoria_historial.py`
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
            print("Accion no reconocida")
    except Exception as e:
        print(f"Error al ejecutar accion: {e}")
```

### 📂 Archivo: `modulos\token_monitor.py`
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
    precio_out = limites.get("precio_output", 0)
    costo = (tokens_input / 1_000_000 * precio_in) + (tokens_output / 1_000_000 * precio_out)
    return round(costo, 6)

def ver_uso():
    log = cargar_log()
    if not log:
        return "No hay registros de uso aun."
    ahora = datetime.datetime.now()
    hoy = ahora.strftime("%Y-%m-%d")
    hora_actual = ahora.strftime("%Y-%m-%d %H:00")
    resultado = f"USO DE TOKENS - {hoy}\n{'='*45}\n"
    costo_total_dia = 0
    for api, data in log.items():
        dia_data = data["dias"].get(hoy, {"input": 0, "output": 0})
        hora_data = data["horas"].get(hora_actual, {"input": 0, "output": 0})
        uso_in_dia = dia_data.get("input", 0)
        uso_out_dia = dia_data.get("output", 0)
        uso_in_hora = hora_data.get("input", 0)
        uso_out_hora = hora_data.get("output", 0)
        costo_dia = calcular_costo(api, uso_in_dia, uso_out_dia)
        costo_total_dia += costo_dia
        limites = LIMITES.get(api, {})
        lim_dia = limites.get("por_dia", -1)
        resultado += f"\n{api.upper()}:\n"
        resultado += f"  Hoy input:   {uso_in_dia:>10,} tokens\n"
        resultado += f"  Hoy output:  {uso_out_dia:>10,} tokens\n"
        if lim_dia > 0:
            total_hoy = uso_in_dia + uso_out_dia
            pct = round(total_hoy / lim_dia * 100, 1)
            resultado += f"  Limite dia:  {lim_dia:>10,} ({pct}% usado)\n"
        resultado += f"  Costo hoy:   ${costo_dia:.6f} USD\n"
        resultado += f"  Esta hora:   {uso_in_hora + uso_out_hora:,} tokens\n"
    resultado += f"\n{'='*45}\n"
    resultado += f"COSTO TOTAL HOY: ${costo_total_dia:.6f} USD\n"
    return resultado

def ver_historial(api=None, dias=7):
    log = cargar_log()
    if not log:
        return "No hay historial de uso"
    resultado = f"HISTORIAL ULTIMOS {dias} DIAS\n{'='*45}\n"
    ahora = datetime.datetime.now()
    costo_total = 0
    for d in range(dias):
        fecha = (ahora - datetime.timedelta(days=d)).strftime("%Y-%m-%d")
        resultado += f"\n{fecha}:\n"
        apis_mostrar = [api] if api else list(log.keys())
        for a in apis_mostrar:
            if a in log:
                dia_data = log[a]["dias"].get(fecha, {"input": 0, "output": 0})
                uso_in = dia_data.get("input", 0)
                uso_out = dia_data.get("output", 0)
                if uso_in + uso_out > 0:
                    costo = calcular_costo(a, uso_in, uso_out)
                    costo_total += costo
                    resultado += f"  {a}: {uso_in:,} input + {uso_out:,} output = ${costo:.6f}\n"
    resultado += f"\nCOSTO TOTAL {dias} DIAS: ${costo_total:.6f} USD\n"
    return resultado

def ver_limites():
    resultado = "LIMITES Y PRECIOS POR API\n" + "="*45 + "\n"
    for api, l in LIMITES.items():
        resultado += f"\n{api.upper()}:\n"
        resultado += f"  Precio input:  ${l['precio_input']}/M tokens\n"
        resultado += f"  Precio output: ${l['precio_output']}/M tokens\n"
        if l['por_dia'] > 0:
            resultado += f"  Limite dia:    {l['por_dia']:,} tokens\n"
        else:
            resultado += f"  Limite dia:    sin limite\n"
    return resultado

def ejecutar(accion, texto):
    t = texto.lower()
    if "historial" in t:
        api = None
        for a in LIMITES.keys():
            if a in t:
                api = a
                break
        return ver_historial(api)
    elif "limite" in t or "precio" in t:
        return ver_limites()
    else:
        return ver_uso()
```

### 📂 Archivo: `modulos\uptime.py`
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

### 📂 Archivo: `orquestador.py`
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
            contenido = data["choices"][0]["message"]["content"]
            if "<think>" in contenido and "</think>" in contenido:
                contenido = contenido.split("</think>")[-1].strip()
            return contenido, modelo
        except Exception:
            continue
    try:
        return preguntar_fn(prompt), "fallback-auto"
    except Exception:
        return None, None

def armar_plan(pedido_usuario, preguntar_fn):
    lista_modulos = "\n".join([f"- {k}: {v}" for k, v in MODULOS_DISPONIBLES.items()])
    prompt = (
        "Sos el orquestador de MECANICO, un agente que analiza y repara codigo Python.\n"
        "Tenes disponibles estos comandos exactos:\n\n"
        f"{lista_modulos}\n\n"
        "Los proyectos del usuario estan en C:/IA/AGENTE/. Si menciona un nombre de proyecto sin ruta completa,\n"
        "asumi que esta en C:/IA/AGENTE/NOMBRE_PROYECTO (ej: MAT.ONE esta en C:/IA/AGENTE/MAT.ONE).\n\n"
        f"El usuario pidio: {pedido_usuario}\n\n"
        "Arma un plan de pasos usando SOLO los comandos de arriba, con sus rutas y parametros reales.\n"
        "IMPORTANTE: si la ruta es una carpeta (no termina en .py ni otra extension), usa 'analizar proyecto <ruta>', NUNCA 'analizar <ruta>' solo para carpetas.\n"
        "Respondé SOLO con un JSON valido con este formato exacto, nada mas:\n"
        '{"pasos": ["comando1 parametro1", "comando2 parametro2"], "explicacion": "breve resumen de lo que se va a hacer"}\n\n'
        "Si el pedido es ambiguo o falta informacion (como una ruta), pedila en el campo explicacion y deja pasos vacio.\n"
        "Responde SOLO el JSON, sin texto antes ni despues, sin backticks."
    )
    respuesta, modelo_usado = intentar_modelos_nvidia(prompt, preguntar_fn)
    if not respuesta:
        return None, None, "ERROR: Ninguna IA pudo armar el plan"
    match = re.search(r'\{.*\}', respuesta, re.DOTALL)
    if not match:
        return None, None, f"ERROR: No se genero un plan valido.\nRespuesta: {respuesta[:300]}"
    try:
        plan = json.loads(match.group())
        return plan.get("pasos", []), plan.get("explicacion", ""), modelo_usado
    except json.JSONDecodeError as e:
        return None, None, f"ERROR: JSON invalido del plan: {e}"

def ejecutar_plan(pasos, modulos_cargados):
    resultados = []
    for i, paso in enumerate(pasos, 1):
        paso_lower = paso.lower().strip()
        resultado = None
        try:
            if paso_lower.startswith("reparar") and "reparador" in modulos_cargados:
                resultado = modulos_cargados["reparador"].ejecutar("reparar", paso)
            elif paso_lower.startswith("mejorar") and "reparador" in modulos_cargados:
                resultado = modulos_cargados["reparador"].ejecutar("mejorar", paso)
            elif paso_lower.startswith("revertir") and "revertir" in modulos_cargados:
                resultado = modulos_cargados["revertir"].ejecutar("revertir", paso)
            elif paso_lower.startswith("analizar") and "analizador" in modulos_cargados:
                resultado = modulos_cargados["analizador"].ejecutar("analizar", paso)
            elif paso_lower.startswith("explorar") and "explorador" in modulos_cargados:
                resultado = modulos_cargados["explorador"].ejecutar("explorar", paso)
            elif paso_lower.startswith("leer") and "lector_contexto" in modulos_cargados:
                resultado = modulos_cargados["lector_contexto"].ejecutar("leer", paso)
            elif paso_lower.startswith("git") and "git_manager" in modulos_cargados:
                resultado = modulos_cargados["git_manager"].ejecutar("git", paso)
            elif paso_lower.startswith("generar") and "generador" in modulos_cargados:
                resultado = modulos_cargados["generador"].ejecutar("generar", paso)
            elif paso_lower.startswith("github") and "github_reader" in modulos_cargados:
                resultado = modulos_cargados["github_reader"].ejecutar("github", paso)
            elif paso_lower.startswith("scout") and "github_scout" in modulos_cargados:
                resultado = modulos_cargados["github_scout"].ejecutar("scout", paso)
            elif paso_lower.startswith("tokens") and "token_monitor" in modulos_cargados:
                resultado = modulos_cargados["token_monitor"].ejecutar("tokens", paso)
            else:
                resultado = f"No se reconoce el comando: {paso}"
        except Exception as e:
            resultado = f"ERROR ejecutando '{paso}': {e}"
        resultados.append(f"[Paso {i}/{len(pasos)}] {paso}\n{resultado}\n")
    return "\n".join(resultados)

```

### 📂 Archivo: `scanner_maestro.py`
```python
import os
from pathlib import Path

def generate_master_context():
    root = Path(__file__).parent
    
    # Carpetas a ignorar COMPLETAMENTE (no listar ni leer su contenido)
    ignore_dirs = {
        "venv", ".git", "__pycache__", "node_modules", 
        "whisper_models", ".venv", "env", "workspace", 
        "session", ".wwebjs_cache", "Cache", "Code Cache", 
        "GPUCache", "GrShaderCache", "DawnGraphiteCache", "DawnWebGPUCache",
        "IndexedDB", "Local Storage", "Service Worker"
    }
    
    output_lines = []
    output_lines.append("# 🧠 MASTER CONTEXT - AGENTE IA MODULAR")
    output_lines.append("Este archivo contiene toda la información necesaria para que cualquier IA entienda, modifique y extienda este proyecto sin perder el hilo ni gastar tokens de más.\n")
    
    # 1. ESTRUCTURA DEL PROYECTO (Árbol de directorios limpio)
    output_lines.append("## 📂 1. ESTRUCTURA DEL PROYECTO\n")
    tree_lines = []
    for path in sorted(root.rglob("*")):
        if any(part in ignore_dirs for part in path.parts):
            continue
        if path.name == "MASTER_CONTEXT.md": # Ignorar el propio archivo de salida
            continue
            
        rel = path.relative_to(root)
        indent = "  " * (len(rel.parts) - 1)
        if path.is_dir():
            tree_lines.append(f"{indent}📁 {rel.name}/")
        else:
            tree_lines.append(f"{indent}📄 {rel.name}")
            
    output_lines.append("```\n" + "\n".join(tree_lines) + "\n```\n")
    
    # 2. ARCHIVOS PRIORITARIOS (Se leen COMPLETOS, sin truncar)
    priority_files = [
        ".env.example",
        "requirements.txt",
        "README.md",
        "GUIA.txt",
        "modules_registry.json",
        "core/config.py",
        "core/model_router.py",
        "core/orchestrator.py",
        "main.py",
        "modules/whatsapp_bot/whatsapp_server/package.json"
    ]
    
    # Agregar dinámicamente todos los specs y módulos
    for path in root.rglob("*"):
        if any(part in ignore_dirs for part in path.parts):
            continue
        
        rel_str = str(path.relative_to(root)).replace("\\", "/")
        
        # Specs (todos los .json dentro de la carpeta specs)
        if path.parent.name == "specs" and path.suffix == ".json":
            priority_files.append(rel_str)
            
        # Módulos (todos los module.py y manifest.json)
        if "modules" in path.parts and path.name in ["module.py", "manifest.json"]:
            priority_files.append(rel_str)

    # Eliminar duplicados y ordenar para consistencia
    priority_files = sorted(list(set(priority_files)))
    
    output_lines.append("## 📄 2. CONTENIDO DE ARCHIVOS CLAVE (COMPLETO)\n")
    
    for file_path in priority_files:
        full_path = root / file_path
        if full_path.exists() and full_path.is_file():
            output_lines.append(f"### 📂 Archivo: `{file_path}`")
            # Detectar extensión para el bloque de código markdown
            ext = file_path.split(".")[-1] if "." in file_path else "text"
            if ext == "py": ext = "python"
            elif ext == "json": ext = "json"
            
            output_lines.append(f"```{ext}")
            try:
                content = full_path.read_text(encoding="utf-8", errors="ignore")
                
                # Seguridad: solo truncar si el archivo es absurdamente grande (> 20,000 caracteres)
                # Tus archivos de código y config normales no llegarán a esto.
                if len(content) > 20000:
                    output_lines.append(content[:10000])
                    output_lines.append("\n\n--- [CONTENIDO TRUNCADO POR TAMAÑO EXCESIVO (>20k caracteres)] ---\n")
                    output_lines.append(content[-5000:])
                else:
                    output_lines.append(content)
            except Exception as e:
                output_lines.append(f"⚠️ Error leyendo el archivo: {e}")
            output_lines.append("```\n")
            
    # 3. INSTRUCCIONES PARA LA IA (Prompt Inicial Integrado)
    output_lines.append("## 🤖 3. INSTRUCCIONES OBLIGATORIAS PARA LA IA")
    output_lines.append("1. **No inventes rutas**: Usa siempre las rutas relativas mostradas en la estructura de carpetas.")
    output_lines.append("2. **Módulos**: Si debes modificar o crear un módulo, sigue estrictamente el formato de `manifest.json` y `module.py` existentes.")
    output_lines.append("3. **Model Router**: Para tareas de IA, usa SIEMPRE `from core import model_router` y `model_router.ask(...)`. Nunca importes librerías de IA (OpenAI, Google, etc.) directamente en los módulos.")
    output_lines.append("4. **Seguridad**: Nunca modifiques el archivo `.env` directamente. Si se necesita una nueva variable, indícalo en tu respuesta para que el usuario la agregue manualmente.")
    output_lines.append("5. **Workspace**: Las operaciones de archivos del usuario (crear, leer, editar) deben ir SIEMPRE a `config.WORKSPACE_DIR` usando el módulo `file_manager`. Para modificar el código del propio proyecto, usa el módulo `project_editor`.")
    output_lines.append("6. **Formato de respuesta**: Cuando generes código nuevo, devuélvelo SIEMPRE en bloques de código markdown con la ruta del archivo en el comentario superior (ej: `# modules/nuevo_modulo/module.py`).")

    # Guardar archivo en la raíz del proyecto
    output_file = root / "MASTER_CONTEXT.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
        
    print("✅ ¡Listo! El contexto maestro se generó exitosamente.")
    print(f"👉 Archivo guardado en: {output_file.resolve()}")
    print("\n💡 PRÓXIMO PASO: Abre el archivo 'MASTER_CONTEXT.md', copia TODO su contenido y pégalo en el chat de cualquier IA. ¡Entenderá el proyecto al 100% desde el primer mensaje!")

if __name__ == "__main__":
    generate_master_context()
```

### 📂 Archivo: `uptime.py`
```python
import logging
import platform
import psutil
import time
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Palabras clave reconocidas
PALABRAS_CLAVE_RECONOCIDAS = ["uptime", "tiempo", "corriendo"]

class Sistema:
    def __init__(self):
        self.boot_time = None

    def obtener_boot_time(self) -> float:
        """Obtiene el tiempo de arranque del sistema"""
        if self.boot_time is None:
            try:
                self.boot_time = psutil.boot_time()
            except Exception as e:
                logging.error(f"Error al obtener el tiempo de arranque: {str(e)}")
                raise
        return self.boot_time

    def calcular_uptime(self) -> str:
        """Calcula el tiempo de actividad del sistema"""
        boot_time = self.obtener_boot_time()
        uptime = time.time() - boot_time
        horas = int(uptime // 3600)
        minutos = int((uptime % 3600) // 60)
        segundos = int(uptime % 60)
        return f"{horas} horas, {minutos} minutos y {segundos} segundos"

    def ejecutar_accion(self, texto: str) -> None:
        """Interpreta el texto y llama a las funciones del módulo"""
        if any(palabra in texto.lower() for palabra in PALABRAS_CLAVE_RECONOCIDAS):
            try:
                uptime = self.calcular_uptime()
                logging.info(f"El sistema lleva {uptime} en ejecución")
            except Exception as e:
                logging.error(f"Error al ejecutar la acción: {str(e)}")
        else:
            logging.info("Acción no reconocida")

def obtener_sistema_operativo():
    """Obtiene el sistema operativo actual"""
    return platform.system()

def obtener_boot_time():
    """Obtiene el tiempo de arranque del sistema"""
    try:
        boot_time = psutil.boot_time()
        return boot_time
    except Exception as e:
        logging.error(f"Error al obtener el tiempo de arranque: {str(e)}")
        return None

def calcular_uptime():
    """Calcula el tiempo de actividad del sistema"""
    boot_time = obtener_boot_time()
    if boot_time is not None:
        uptime = time.time() - boot_time
        return uptime
    else:
        return None

def obtener_uptime_en_horas(uptime):
    """Convierte el uptime a horas, minutos y segundos"""
    if uptime is not None:
        horas = int(uptime // 3600)
        minutos = int((uptime % 3600) // 60)
        segundos = int(uptime % 60)
        return f"{horas} horas, {minutos} minutos y {segundos} segundos"
    else:
        return None

def ejecutar(accion, texto):
    """Interpreta el texto y llama a las funciones del modulo"""
    palabras = texto.lower().split()
    if "uptime" in texto or "tiempo" in texto or "corriendo" in texto:
        try:
            uptime = calcular_uptime()
            uptime_en_horas = obtener_uptime_en_horas(uptime)
            if uptime_en_horas is not None:
                logging.info(f"El sistema lleva {uptime_en_horas} en ejecución")
            else:
                logging.info("No se pudo calcular el uptime")
        except Exception as e:
            logging.error(f"Error al ejecutar la acción: {str(e)}")
    else:
        logging.info("Acción no reconocida")

# Ejemplo de uso:
sistema = Sistema()
sistema.ejecutar_accion("Cuanto tiempo lleva corriendo el sistema")
ejecutar("calcular", "Cuanto tiempo lleva corriendo el sistema")
```

## 🤖 3. DIRECTRICES DE DESARROLLO E INSTRUCCIONES PARA LA IA
Al sugerir cambios, resolver bugs o escribir nuevas características para este proyecto, debes respetar las siguientes reglas obligatorias:

1. **Respetar Rutas:** Trabaja siempre bajo el esquema de archivos y carpetas definido en la sección de estructura.
2. **Consistencia de Estilo:** Analiza los lenguajes, tabulaciones y el estilo de programación usado en los archivos mostrados antes de generar nuevas líneas de código.
3. **Gestión de Dependencias:** Si necesitas librerías externas adicionales, no las importes directamente sin advertir al usuario. Indica explícitamente qué dependencias deben agregarse en los archivos correspondientes (por ejemplo, `requirements.txt` o `package.json`).
4. **Seguridad y Credenciales:** Nunca expongas ni guardes contraseñas, tokens o claves API directamente en el código de producción. Promueve siempre el uso de variables de entorno (ej: `.env`).
5. **Formato de Entrega de Código:** Cuando propongas modificaciones o código nuevo, especifica la ruta destino en un comentario en la cabecera del bloque de código (ej: `# /ruta/al/archivo.py` o `// /ruta/al/archivo.js`).
6. **Evitar Código Fantasma:** No dejes funciones a medias con comentarios `// agregar lógica aquí` o `pass`. Si reescribes una estructura de código, asegúrate de que sea funcional y esté autocontenida.