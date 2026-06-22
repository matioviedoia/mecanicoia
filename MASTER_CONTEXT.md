# 🧠 MASTER CONTEXT - AGENTE IA MODULAR
Este archivo contiene toda la información necesaria para que cualquier IA entienda, modifique y extienda este proyecto sin perder el hilo ni gastar tokens de más.

## 📂 1. ESTRUCTURA DEL PROYECTO

```
📄 .env
📄 .gitignore
📁 apis/
📄 config.py
📁 logs/
  📁 errors/
    📄 errores.log
📄 MANUAL_MECANICO.md
📄 mecanico (1).py
📁 memoria/
  📁 backups/
    📄 analizador.py.backup_20260620_082455
    📄 analizador.py.backup_20260620_083118
    📄 analizador.py.backup_20260620_083128
    📄 autoeditor.py.backup_20260620_083034
    📄 config.py.backup_20260622_165457
    📄 config.py.backup_20260622_165527
    📄 mecanico.py.backup_20260620_080934
    📄 mecanico.py.backup_20260620_083412
    📄 mecanico.py.backup_20260621_212255
    📄 mecanico.py.backup_20260622_165603
  📁 errores/
    📄 errores.log
  📁 sesiones/
📁 modulos/
  📄 analizador.py
  📄 autoeditor.py
  📄 explorador.py
  📄 git_manager.py
  📄 reparador.py
  📄 revertir.py
📁 Nueva carpeta/
  📄 mecanico.py
📁 proyectos/
📄 scanner_maestro.py
```

## 📄 2. CONTENIDO DE ARCHIVOS CLAVE (COMPLETO)

## 🤖 3. INSTRUCCIONES OBLIGATORIAS PARA LA IA
1. **No inventes rutas**: Usa siempre las rutas relativas mostradas en la estructura de carpetas.
2. **Módulos**: Si debes modificar o crear un módulo, sigue estrictamente el formato de `manifest.json` y `module.py` existentes.
3. **Model Router**: Para tareas de IA, usa SIEMPRE `from core import model_router` y `model_router.ask(...)`. Nunca importes librerías de IA (OpenAI, Google, etc.) directamente en los módulos.
4. **Seguridad**: Nunca modifiques el archivo `.env` directamente. Si se necesita una nueva variable, indícalo en tu respuesta para que el usuario la agregue manualmente.
5. **Workspace**: Las operaciones de archivos del usuario (crear, leer, editar) deben ir SIEMPRE a `config.WORKSPACE_DIR` usando el módulo `file_manager`. Para modificar el código del propio proyecto, usa el módulo `project_editor`.
6. **Formato de respuesta**: Cuando generes código nuevo, devuélvelo SIEMPRE en bloques de código markdown con la ruta del archivo en el comentario superior (ej: `# modules/nuevo_modulo/module.py`).