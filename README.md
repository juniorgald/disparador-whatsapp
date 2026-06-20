# Disparador de Mensagens WhatsApp

Projeto Python que lê contatos cadastrados no Supabase e envia mensagens personalizadas via Z-API para o WhatsApp.

## Pré-requisitos

- Python 3 instalado
- Conta no [Supabase](https://supabase.com)
- Conta na [Z-API](https://z-api.io)

## Setup do Supabase

1. Crie uma conta e um projeto no Supabase
2. Crie uma tabela chamada `contatos` com as colunas `nome` e `telefone` (ambas do tipo text)
3. Insira os contatos pelo painel do Supabase
4. O telefone deve seguir o formato `55` + DDD + número. Exemplo: `5587999999999`
5. Copie a URL do projeto e a Secret Key nas configurações de API

## Setup da Z-API

1. Crie uma conta na Z-API e crie uma instância
2. Escaneie o QR Code com seu WhatsApp para conectar
3. Copie o ID da instância e o Token

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=url_do_seu_projeto
SUPABASE_KEY=sua_secret_key
ZAPI_INSTANCE_ID=id_da_sua_instancia
ZAPI_TOKEN=token_da_sua_instancia
```

## Como rodar

```bash
git clone https://github.com/juniorgald/disparador-whatsapp.git
cd disparador-whatsapp
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```