# Discord Bot

Este repositório contém um bot simples para Discord criado com `discord.py`.

## Requisitos

- Python 3.10+
- Uma conta de bot no Discord

## Instalação

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o token do bot:
   - Copie o arquivo `.env.example` para `.env`
   - Coloque o token real no campo `DISCORD_TOKEN`

4. Inicie o bot:
   ```bash
   python main.py
   ```

## Comandos

- `!ping` → responde com `Pong!`
- `!hello` → envia uma mensagem de saudação
- `!status` → verifica se o bot está online

## Como criar um bot no Discord

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Crie um novo aplicativo
3. Vá em `Bot` e clique em `Add Bot`
4. Copie o token e coloque em `.env`
5. No painel, vá em `OAuth2 > URL Generator`
6. Selecione as permissões do bot e gere um link para convidá-lo ao servidor
