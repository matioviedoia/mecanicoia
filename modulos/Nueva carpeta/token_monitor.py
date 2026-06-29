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
