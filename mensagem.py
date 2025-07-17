import requests


def enviar_alerta_discord(mensagem, webhook_url):
    payload = {'content': mensagem}
    response = requests.post(webhook_url, json=payload)
    print(f"Status: {response.status_code} | Resposta: {response.text}")


DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1392128201387540590/tUhnYxXPYFD8I4KllInc7i-9hfEjPn72MyZOp4nUYug0X21lc-W71D5orudNBYQbAXgb'

mensagem = "🚨 NOVO ALERTA: SIGNUSDT subiu 1% em 1 minuto! Avaliar SHORT."

enviar_alerta_discord(mensagem, DISCORD_WEBHOOK_URL)
