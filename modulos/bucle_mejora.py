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
