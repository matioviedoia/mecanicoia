# 🔧 MANUAL DE USO - MECANICO IA

## ¿Qué es MECANICO?
MECANICO es un agente IA especializado en analizar, reparar y mejorar código.
Usa múltiples APIs de IA (Groq, Gemini, Cerebras, Ollama) y puede trabajar
en cualquier proyecto de tu PC.

---

## 🚀 Cómo arrancar

```
cd C:\IA\AGENTE\MECANICO
python mecanico.py
```

---

## 📋 Modos disponibles

| Modo | Descripción |
|------|-------------|
| **1. Manual** | Vos le decís qué hacer |
| **2. Auto** | MECANICO trabaja solo (en construcción) |
| **3. Consenso** | Todas las APIs responden juntas |
| **4. Ver APIs** | Estado de las APIs conectadas |

---

## 💬 Comandos en Modo Manual

### 🔍 ANALIZAR
Analiza archivos o proyectos buscando errores de sintaxis.

```
analizar C:/ruta/archivo.py
analizar proyecto C:/ruta/proyecto
analizar ia C:/ruta/archivo.py     ← usa IA para análisis profundo
```

### 🔧 REPARAR
Repara un archivo usando IA. Hace backup automático antes.

```
reparar C:/ruta/archivo.py
```

### ↩️ REVERTIR
Restaura un archivo a su versión anterior.

```
revertir mecanico.py               ← revierte al backup más reciente
revertir listar mecanico.py        ← muestra backups disponibles
```

### 📁 EXPLORAR (próximamente)
Navega y trabaja con cualquier carpeta del sistema.

```
explorar listar C:/ruta
explorar buscar archivo.py C:/ruta
explorar leer C:/ruta/archivo.py
explorar info C:/ruta/archivo.py
explorar copiar origen destino
explorar mover origen destino
```

### 🤖 EJECUTAR JSON (Autoeditor)
Crea o modifica archivos usando IA. El comando más poderoso.

#### Crear un módulo nuevo:
```
ejecutar json {"accion": "crear_modulo", "archivo": "modulos/nuevo.py", "contenido": "codigo aqui", "backup": false}
```

#### Crear un archivo:
```
ejecutar json {"accion": "crear_archivo", "archivo": "workspace/notas.txt", "contenido": "contenido aqui", "backup": false}
```

#### Modificar un archivo con IA:
```
ejecutar json {"accion": "modificar_con_ia", "archivo": "modulos/archivo.py", "descripcion": "que queres que cambie", "backup": true}
```

#### Leer un archivo:
```
ejecutar json {"accion": "leer_archivo", "archivo": "config.py"}
```

### 🔀 GIT
Operaciones de Git integradas.

```
git estado        ← ver qué cambió
git push          ← subir todo a GitHub
git historial     ← ver últimos commits
git commit        ← hacer commit sin push
```

### 📊 APIS
Ver el estado de todas las APIs.

```
apis
```

### 🌐 CONSENSO
Preguntarle a todas las APIs al mismo tiempo.
Elegí la opción **3** en el menú.

---

## 🔑 APIs disponibles

| API | Modelo | Velocidad | Uso |
|-----|--------|-----------|-----|
| **Groq** | llama-3.3-70b | ⚡⚡⚡ muy rápido | Respuestas rápidas |
| **Gemini** | gemini-2.5-flash | ⚡⚡ rápido | Análisis complejo |
| **Cerebras** | gpt-oss-120b | ⚡⚡ rápido | Alternativa potente |
| **Ollama** | gemma3:4b | ⚡ local | Sin internet, privado |

---

## 📂 Estructura de carpetas

```
C:\IA\AGENTE\MECANICO\
├── mecanico.py          ← núcleo principal
├── config.py            ← configuración y APIs
├── .env                 ← API keys (nunca compartir)
├── modulos\
│   ├── autoeditor.py    ← crea y modifica archivos con IA
│   ├── analizador.py    ← analiza proyectos
│   ├── reparador.py     ← repara código con IA
│   ├── revertir.py      ← restaura backups
│   ├── git_manager.py   ← maneja Git
│   └── explorador.py    ← navega el sistema
├── memoria\
│   ├── backups\         ← copias antes de cada cambio
│   ├── errores\         ← log de errores
│   └── sesiones\        ← historial
└── workspace\           ← carpeta de trabajo
```

---

## ⚠️ Reglas importantes

1. **MECANICO nunca borra archivos** sin confirmación
2. **Siempre hace backup** antes de modificar
3. **Si algo falla** → usar `revertir archivo.py`
4. **Los errores** se guardan en `memoria/errores/errores.log`
5. **Cada cambio** se guarda en Git automáticamente

---

## 🆘 Si algo sale mal

**Ver el log de errores:**
```
type C:\IA\AGENTE\MECANICO\memoria\errores\errores.log
```

**Revertir un archivo:**
```
revertir mecanico.py
```

**Ver historial de Git:**
```
cd C:\IA\AGENTE\MECANICO
git log --oneline
```

**Volver a una versión anterior en Git:**
```
git checkout HASH -- archivo.py
```

---

## 💡 Ejemplos de uso real

**Analizar y reparar MAT.ONE:**
```
analizar proyecto C:/IA/AGENTE/MAT.ONE
reparar C:/IA/AGENTE/MAT.ONE/mat_one.py
```

**Crear un módulo nuevo:**
```
ejecutar json {"accion": "crear_modulo", "archivo": "modulos/nuevo.py", "contenido": "def ejecutar(accion, texto):\n    return 'hola'", "backup": false}
```

**Modificar config con IA:**
```
ejecutar json {"accion": "modificar_con_ia", "archivo": "config.py", "descripcion": "Agregar nueva API llamada zai con modelo zai-glm-4.7", "backup": true}
```
