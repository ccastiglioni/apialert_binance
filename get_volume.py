import requests

url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,  # você pode paginar para pegar mais
    'page': 1,
}
response = requests.get(url, params=params)
coins = response.json()
PARES_MONITORADOS = [
    f"{coin['symbol'].upper()}USDT"
    for coin in coins
    if coin['market_cap'] and coin['market_cap'] > 200_000_000
]
print(PARES_MONITORADOS)
