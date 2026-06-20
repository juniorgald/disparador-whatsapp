from dotenv import load_dotenv
from supabase import create_client
import os

import requests

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.table("contatos").select("*").execute()

contatos = response.data

print(contatos)

for contato in contatos:
    nome = contato['nome']
    telefone = contato['telefone']
    mensagem = f"Olá {nome} tudo bem com você?"

    url = f"https://api.z-api.io/instances/{os.getenv('ZAPI_INSTANCE_ID')}/token/{os.getenv('ZAPI_TOKEN')}/send-text"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    response = requests.post(url, json=payload)

    print(f"Enviando para {nome}... Status: {response.status_code}")


