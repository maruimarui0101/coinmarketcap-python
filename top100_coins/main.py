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

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}
params = {
    'convert': convert
    , 'sort': 'price'
    , 'limit': 100
}

request = requests.get(listings_url, headers=headers, params=params)
results = request.json()
data = results['data']


table = PrettyTable(['Rank', 'Asset', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])

for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quote'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        if hour_change is not None:
            if hour_change > 0:
                hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change is not None:
            if day_change > 0:
                day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change is not None:
            if week_change > 0:
                week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        if volume is not None:
            volume_string = '{:,}'.format(volume)

        if market_cap is not None:
            market_cap_string = '{:,}'.format(market_cap)

        table.add_row([rank,
                       name + ' ( ' + symbol + ')',
                       '£' + str(price),
                       '£' + str(market_cap),
                       '£' + volume_string,
                       str(hour_change),
                       str(day_change),
                       str(week_change)])

print()
print(table)
print()