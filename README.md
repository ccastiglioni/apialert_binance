# 📈 Altcoin Pump Detector — Scalping Bot com Alertas no Discord

Este projeto é um bot em Python que monitora variações abruptas (pumps) em altcoins listadas na Binance, analisando candles de 1 minuto. Quando uma criptomoeda sobe mais que um valor definido (ex: 3%), o bot envia um alerta automaticamente para um canal no Discord via Webhook.

---

## 🚀 Funcionalidades

- Monitora qualquer par de trading da Binance com base em USDT.
- Detecta pumps com base na variação percentual do candle.
- Envia alertas automáticos para o Discord.
- Totalmente configurável: pares, intervalo, porcentagem mínima.
- Baseado apenas na API pública da Binance (sem necessidade de API Key).
- Pode ser executado em loop contínuo via terminal ou como serviço `systemd`.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia        | Descrição                         |
|-------------------|-----------------------------------|
| Python 3.10+      | Linguagem principal                |
| `python-binance`  | Cliente oficial da API da Binance |
| `requests`        | Envio de alertas para Webhook do Discord |
| Discord Webhooks  | Canal de notificação              |

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/altcoin-scalping-bot.git
cd altcoin-scalping-bot
```

### Crie um ambiente virtual (opcional, mas recomendado)
```bash
python3 -m venv venv
source venv/bin/activate
```

###  Instale as dependências
```bash
pip install requests python-binance
```

###  Webhook do Discor, no seu servidor do Discord:
- Vá até o canal desejado.
- Envia alertas automáticos para o Discord.
- Clique em Editar canal > Integrações > Webhooks.
- Crie um novo webhook e copie o link.
- No código alerta.py, substitua o valor de DISCORD_WEBHOOK_URL pelo seu link de webhook:
```bash
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/SEU_WEBHOOK_AQUI'
```

### Parâmetros principais
```bash
VARIACAO_MINIMA = 3  # porcentagem mínima para enviar alerta
INTERVALO_CANDLE = Client.KLINE_INTERVAL_1MINUTE
INTERVALO_CHECAGEM = 60  # segundos entre cada verificação

PARES_MONITORADOS = [
    'SIGNUSDT', 'DOGEUSDT', 'PEPEUSDT', ...
]
```


###  Execução
```bash
python alerta.py
```
