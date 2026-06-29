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