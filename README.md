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
