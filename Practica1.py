# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:17:14 2024

@author: marti
"""

''' Consultar Información de Criptomonedas con CoinGecko '''
import requests
import json

fechas = ["01-01-2024", "01-07-2024"]
result = []

for fecha in fechas:
    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/history?date={fecha}'
    response = requests.get(url)
    data = response.json()
    datos = {}
    datos["usd"] = data["market_data"]["current_price"]["usd"]
    datos["eur"] = data["market_data"]["current_price"]["eur"]
    result.append(datos)


with open("bitcoin_historical_data.json","w") as out_file:
    json.dump(result, out_file, indent=4)

