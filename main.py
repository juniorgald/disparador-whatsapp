from dotenv import load_dotenv
from supabase import create_client
import requests
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    try:
        response = supabase.table("contatos").select("*").execute()
        logging.info(f"{len(response.data)} contato(s) encontrado(s) no banco.")
        return response.data
    except Exception as e:
        logging.error(f"Erro ao buscar contatos: {e}")
        return []

def enviar_mensagem(contato):
    nome = contato['nome']
    telefone = contato['telefone']
    mensagem = f"Olá, {nome} tudo bem com você?"

    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logging.info(f"Mensagem enviada com sucesso para {nome} ({telefone})")
        else:
            logging.warning(f"Falha ao enviar para {nome}. Status: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem para {nome}: {e}")

def main():
    logging.info("Iniciando disparador de mensagens...")
    contatos = buscar_contatos()

    if not contatos:
        logging.warning("Nenhum contato encontrado. Encerrando.")
        return

    for contato in contatos:
        enviar_mensagem(contato)

    logging.info("Envio concluído.")

main()