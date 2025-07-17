from binance.client import Client
import requests
import time
from pprint import pprint
# ================================
# CONFIGURAÇÕES
# ================================

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1392128201387540590/tUhnYxXPYFD8I4KllInc7i-9hfEjPn72MyZOp4nUYug0X21lc-W71D5orudNBYQbAXgb'
VARIACAO_MINIMA = 1  # Porcentagem mínima de pump para gerar alerta
INTERVALO_CANDLE = Client.KLINE_INTERVAL_1MINUTE
INTERVALO_CHECAGEM = 60  # Tempo entre verificações (em segundos)

PARES_MONITORADOS = [
    'SIGNUSDT',
    'DOGEUSDT',
    'PEPEUSDT',
    'SHIBUSDT',
    'PENDLEUSDT',
    'HUMAUSDT',
    'QNTUSDT',
    # Adicione mais pares se quiser
]


def my_printDebug(ultimo_candle):
    pprint(f"Número de trades realizados no candle:  {ultimo_candle[8]}")
    pprint(f"Volume comprado a mercado:  {ultimo_candle[9]}")
    exit()


def enviar_alerta_discord(mensagem):
    payload = {'content': mensagem}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code != 204:
            print(f"[ERRO] Falha ao enviar alerta: {response.text}")
    except Exception as e:
        print(f"[ERRO] Exceção ao enviar alerta: {e}")

# ================================
# FUNÇÃO PRINCIPAL: Monitorar pumps
# ================================


def monitorar_pumps():
    print("Entrou na função monitorar_pumps()")  # Debug
    client = Client(requests_params={'timeout': 5})
    print(" Bot de scalping iniciado. Monitorando pares...\n")

    while True:
        for par in PARES_MONITORADOS:
            try:
                print(f"\n Verificando par: {par}")
                candles = client.get_klines(symbol=par, interval=INTERVALO_CANDLE, limit=2)
                ultimo_candle = candles[-2]

                my_printDebug(ultimo_candle)

                open_price = float(ultimo_candle[1])
                close_price = float(ultimo_candle[4])
                variacao = ((close_price - open_price) / open_price) * 100

                print(f" Abertura: {open_price} | Fechamento: {close_price} | Variação: {variacao:.2f}%")

                if variacao >= VARIACAO_MINIMA:
                    mensagem = f" ALERTA: {par} subiu {variacao:.2f}% em 1 minuto! Avaliar SHORT."
                    print(f" Enviando alerta: {mensagem}")
                    enviar_alerta_discord(mensagem)
                else:
                    print(f" Sem pump suficiente (mínimo {VARIACAO_MINIMA}%)")

            except Exception as e:
                print(f"[ERRO] Falha ao monitorar {par}: {e}")
                time.sleep(5)

        print(f"\n Aguardando {INTERVALO_CHECAGEM} segundos...\n")
        time.sleep(INTERVALO_CHECAGEM + 3)  # Adiciona 3 segundos de margem

# ================================
# EXECUÇÃO DIRETA
# ================================


if __name__ == '__main__':
    monitorar_pumps()
