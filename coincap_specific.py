import requests, json
import os
import config

symbols_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
quotes_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}

request = requests.get(symbols_url, headers=headers)
results = request.json()
data = results['data']

ticker_pairs = {currency['symbol']: currency['id'] for currency in data}

# print(ticker_pairs)
while True:
    search_symbol = input('Enter cryptocurrency symbol: ')
    search_id = ticker_pairs[search_symbol.upper()]
    request = requests.get(quotes_url, headers=headers, params={'id': search_id})
    results = request.json()
    data = results['data'][str(search_id)]

    name = data['name']
    symbol = data['symbol']

    quotes = data['quote']['USD']
    market_cap = quotes['market_cap']
    percent_change_1h = quotes['percent_change_1h']
    percent_change_24h = quotes['percent_change_24h']
    percent_change_7d = quotes['percent_change_7d']
    price = quotes['price']
    volume_24h = quotes['volume_24h']

    print(name)
    print(symbol)
    print(price)

    if input('would you like to search with another coin? ') == 'n':
        break
    else:
        continue





