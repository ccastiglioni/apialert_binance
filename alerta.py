from binance.client import Client
import requests
import time

# ================================
# CONFIGURAÇÕES
# ================================

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1392128201387540590/tUhnYxXPYFD8I4KllInc7i-9hfEjPn72MyZOp4nUYug0X21lc-W71D5orudNBYQbAXgb'
VARIACAO_MINIMA = 3  # Porcentagem mínima de pump para gerar alerta
INTERVALO_CANDLE = Client.KLINE_INTERVAL_1MINUTE
INTERVALO_CHECAGEM = 20  # Tempo entre verificações (em segundos)

# erro :  KASUSDT , SPXUSDT, METHUSDT , PUMPUSDT , DEEPUSDT XCNUSDT  POPCATUSDT
PARES_MONITORADOS = [
    'BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'BABYUSDT', 'BNBUSDT', 'SOLUSDT', 'USDCUSDT', 'DOGEUSDT', 'NEIROUSDT', 'TRXUSDT',
    'ADAUSDT', 'WBTCUSDT', 'XLMUSDT', 'SUIUSDT', 'LINKUSDT', 'HBARUSDT', 'BCHUSDT', 'AVAXUSDT', 'LTCUSDT', 'SHIBUSDT',
    'TONUSDT', 'USDSUSDT', 'UNIUSDT', 'DOTUSDT', 'XMRUSDT', 'PEPEUSDT', 'BGBUSDT', 'AAVEUSDT', 'TAOUSDT',
    'DAIUSDT', 'ETCUSDT', 'NEARUSDT', 'ONDOUSDT', 'ENAUSDT', 'APTUSDT', 'ICPUSDT', 'KASUSDT', 'BONKUSDT', 'PENGUUSDT',
    'ALGOUSDT', 'ARBUSDT', 'USD1USDT', 'VETUSDT', 'ATOMUSDT', 'RENDERUSDT', 'POLUSDT', 'WLDUSDT', 'TRUMPUSDT',
    'FETUSDT', 'SEIUSDT', 'BNSOLUSDT', 'FILUSDT', 'QNTUSDT', 'SPXUSDT', 'JUPUSDT', 'IPUSDT', 'FARTCOINUSDT',
    'FDUSDUSDT', 'METHUSDT', 'CRVUSDT', 'TIAUSDT', 'INJUSDT', 'NEXOUSDT', '1000FLOKIUSDT', 'STXUSDT', 'FLOKIUSDT',
    'OPUSDT', 'SUSDT', 'WIFUSDT', 'IMXUSDT', 'GRTUSDT', 'VIRTUALUSDT', 'PUMPUSDT', 'USDCUSDT', 'LDOUSDT', 'KAIAUSDT',
    'ENSUSDT', 'PAXGUSDT', 'WBTCUSDT', 'XTZUSDT', 'AUSDT', 'CAKEUSDT', 'CFXUSDT', 'THETAUSDT', 'RAYUSDT', 'PYUSDUSDT',
    'JASMYUSDT', 'IOTAUSDT', 'GALAUSDT', 'AEROUSDT', 'SANDUSDT', 'PENDLEUSDT', 'PYTHUSDT', 'JTOUSDT', 'BTTUSDT',
    'ZECUSDT', 'FLOWUSDT', 'HNTUSDT', 'WETHUSDT', 'DOGEUSDT', 'WALUSDT', 'MANAUSDT', '1000000MOGUSDT', 'BUSDT',
    'BSVUSDT', 'BRETTUSDT', 'SYRUPUSDT', 'WETHUSDT', 'CBETHUSDT', 'XCNUSDT', 'USDDUSDT', 'APEUSDT', 'RSRUSDT',
    'RUNEUSDT', 'TUSDUSDT', 'ARUSDT', 'ETHFIUSDT', 'DYDXUSDT', 'SDAIUSDT', 'STRKUSDT', 'EGLDUSDT', 'NEOUSDT',
    'COMPUSDT', 'DEEPUSDT', '1000XECUSDT', 'WEMIXUSDT', 'KAVAUSDT', 'AXSUSDT', 'BEAMUSDT', 'EIGENUSDT', 'CVXUSDT',
    'AXLUSDT', 'DEXEUSDT', 'CHZUSDT', 'SPKUSDT', 'ZKUSDT', 'STHYPEUSDT', 'DAIUSDT', 'EOSUSDT', '1INCHUSDT',
    'WUSDT', 'GNOUSDT', 'AKTUSDT', 'POPCATUSDT', 'MOVEUSDT', 'JSTUSDT', 'SUPERUSDT', 'SUNUSDT', 'ATHUSDT', 'TURBOUSDT',
    'LUNCUSDT', 'WBTCUSDT', 'MATICUSDT', 'KAITOUSDT', 'TWTUSDT', 'AMPUSDT', 'MEWUSDT']

# ================================
# FUNÇÃO: Enviar mensagem para o Discord
# ================================


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
                time.sleep(2)

        print(f"\n Aguardando {INTERVALO_CHECAGEM} segundos...\n")
        time.sleep(INTERVALO_CHECAGEM + 2)  # Adiciona 2 segundos de margem

# ================================
# EXECUÇÃO DIRETA
# ================================


if __name__ == '__main__':
    monitorar_pumps()
