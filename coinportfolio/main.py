import os 
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

import sys
sys.path.insert(0, '..')
import config

convert = 'GBP'

symbols_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
quotes_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}
params = {
    'convert': convert
}

request = requests.get(symbols_url, headers=headers)
results = request.json()
data = results['data']

ticker_pairs = {currency['symbol']: currency['id'] for currency in data}

print()
print('MY PORTFOLIO')
print()

portfolio_value = 0.0
last_updated = 0

table  = PrettyTable(['Asset', 'Amount Owned', convert + ' Value', 'Price', '1h', '24h', '7d'])

with open('portfolio.txt') as inp:
  for line in inp:
    ticker, amt = line.split(',')
    ticker = ticker.upper()

    _id = ticker_pairs[ticker]

    request = requests.get(quotes_url, headers=headers, params={'id': _id})
    results = request.json()
    data = results['data'][str(_id)]

    name = data['name']
    symbol = data['symbol']

    quotes = data['quote']['USD']
    market_cap = quotes['market_cap']
    percent_change_1h = quotes['percent_change_1h']
    percent_change_24h = quotes['percent_change_24h']
    percent_change_7d = quotes['percent_change_7d']
    price = quotes['price']
    volume_24h = quotes['volume_24h']

    value = float(price) + float(amt)

    if percent_change_1h > 0:
            percent_change_1h = Back.GREEN + str(percent_change_1h) + '%' + Style.RESET_ALL
    else:
        percent_change_1h = Back.RED + str(percent_change_1h) + '%' + Style.RESET_ALL

    if percent_change_24h > 0:
        percent_change_24h = Back.GREEN + str(percent_change_24h) + '%' + Style.RESET_ALL
    else:
        percent_change_24h = Back.RED + str(percent_change_24h) + '%' + Style.RESET_ALL

    if percent_change_7d > 0:
        percent_change_7d = Back.GREEN + str(percent_change_7d) + '%' + Style.RESET_ALL
    else:
        percent_change_7d = Back.RED + str(percent_change_7d) + '%' + Style.RESET_ALL

    portfolio_value += value

    value_string = '{:,}'.format(round(value,2))

    table.add_row([name + ' (' + symbol + ')',
                    amt,
                    '£' + value_string,
                    '£' + str(price),
                    str(percent_change_1h),
                    str(percent_change_24h),
                    str(percent_change_7d)])

print(table)
print()