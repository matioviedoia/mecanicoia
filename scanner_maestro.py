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