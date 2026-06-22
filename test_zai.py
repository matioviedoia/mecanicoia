import requests
from dotenv import load_dotenv
import os
import json

load_dotenv("C:/IA/AGENTE/MECANICO/.env")

key = os.getenv("ZAI_API_KEY")

headers = {
    "Authorization": key,
    "Content-Type": "application/json"
}

body = {
    "model": "glm-4.7-flash",
    "messages": [{"role": "user", "content": "hola"}],
    "max_tokens": 100
}

r = requests.post("https://open.bigmodel.cn/api/paas/v4/chat/completions", headers=headers, json=body, timeout=30)
print(json.dumps(r.json(), indent=2))
