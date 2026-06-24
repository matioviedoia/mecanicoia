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
