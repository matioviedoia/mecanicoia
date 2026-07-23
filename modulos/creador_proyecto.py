import os
import json

# Lista de palabras clave
KEYWORDS = ["proyecto", "codigo", "python", "node", "javascript"]

def crear_proyecto(nombre, codigo):
    """
    Crea un proyecto nuevo con el nombre y el codigo proporcionados.
    
    :param nombre: Nombre del proyecto
    :param codigo: Codigo del proyecto
    :return: Ruta de la carpeta creada y el archivo generado
    """
    try:
        # Crear carpeta para el proyecto
        ruta_proyecto = f"C:/IA/AGENTE/proyectos_generados/{nombre}"
        os.makedirs(ruta_proyecto, exist_ok=True)
        
        # Determinar el nombre del archivo segun la descripcion
        if "python" in nombre.lower():
            nombre_archivo = "main.py"
        elif "node" in nombre.lower() or "javascript" in nombre.lower():
            nombre_archivo = "index.js"
        else:
            nombre_archivo = "main.py"
        
        # Guardar el codigo en el archivo
        ruta_archivo = f"{ruta_proyecto}/{nombre_archivo}"
        with open(ruta_archivo, "w") as archivo:
            archivo.write(codigo)
        
        # Retornar la ruta de la carpeta y el archivo generado
        return f"Proyecto creado en {ruta_proyecto} con archivo {nombre_archivo}"
    
    except Exception as e:
        return f"Error al crear proyecto: {str(e)}"

def obtener_codigo(descripcion, preguntar_fn):
    prompt = f"Escreva el código para el proyecto {descripcion}"
    resultado = preguntar_fn(prompt)
    from modulos.generador import extraer_codigo
    codigo_proceso = extraer_codigo(resultado)
    return codigo_proceso

def ejecutar(accion, texto):
    """
    Interpreta el texto y llama a las funciones del modulo.
    :param accion: Trigger del modulo
    :param texto: Descripcion del proyecto
    :return: Reporte de la accion realizada
    """
    try:
        from mecanico import preguntar
        if any(palabra in texto.lower() for palabra in KEYWORDS):
            nombre_proyecto = texto.split()[-1]
            codigo_proyecto = obtener_codigo(texto, preguntar)
            reporte = crear_proyecto(nombre_proyecto, codigo_proyecto)
            return reporte
        else:
            return "No se reconocen palabras clave en la descripcion"
    except Exception as e:
        return f"Error al ejecutar accion: {str(e)}"