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
