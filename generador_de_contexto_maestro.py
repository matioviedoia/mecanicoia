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