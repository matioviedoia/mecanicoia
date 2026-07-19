import pyperclip
import json
import os

# Lista de palabras clave para el modulo
KEYWORDS = ['copiar', 'portapapeles', 'clipboard']

def copiar_a_portapapeles(texto):
    """
    Copia el contenido al portapapeles de Windows.
    
    Args:
        texto (str): El texto a copiar.
    
    Returns:
        str: Mensaje de confirmación del copiado.
    """
    try:
        pyperclip.copy(texto)
        return "Ya tenes en tu portapapeles el texto, pegalo con Ctrl mas V."
    except Exception as e:
        return f"Error al copiar texto al portapapeles: {str(e)}"

def ejecutar(accion, texto):
    """
    Interpreta el texto y llama a las funciones del modulo.
    
    Args:
        accion (str): El nombre del trigger del modulo (no se utiliza).
        texto (str): El texto a interpretar.
    
    Returns:
        str: Mensaje de resultado de la operación.
    """
    try:
        # Buscar palabras clave en el texto
        if 'copiar' in texto.lower() or 'portapapeles' in texto.lower() or 'clipboard' in texto.lower():
            # Extraer el texto a copiar del mensaje
            palabras = texto.split()
            texto_a_copiar = palabras[-1]
            if os.path.exists(texto_a_copiar):
                with open(texto_a_copiar, 'r', encoding='utf-8') as archivo:
                    contenido_del_archivo = archivo.read()
                    return copiar_a_portapapeles(contenido_del_archivo)
            else:
                return copiar_a_portapapeles(texto_a_copiar)
        else:
            return "No se encontraron palabras clave en el texto."
    except Exception as e:
        return f"Error al interpretar el texto: {str(e)}"