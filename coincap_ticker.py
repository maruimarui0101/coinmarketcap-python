import requests, json
import config

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}

limit = 100
start = 1
sort = 'name'
convert = 'GBP'

choice = input('Would you like to change the request parameters?')

if choice == 'y':
    limit = input('Input limit: ')
    start = input('Input start: ')
    sort = input('Sort by? ')
    convert = input('What is your local currency? ')


params = {
    'limit': limit
    , 'start': start
    , 'sort': sort
    , 'convert': convert 
}

request = requests.get(listings_url, headers=headers, params=params)
results = request.json()

for currency in results['data']: 
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']

    circulating_supply = currency['circulating_supply']
    total_supply = currency['total_supply']

    quotes = currency['quote'][convert]
    market_cap = quotes['market_cap']
    percent_change_1h = quotes['percent_change_1h']
    percent_change_24h = quotes['percent_change_24h']
    percent_change_7d = quotes['percent_change_7d']
    price = quotes['price']
    volume_24h = quotes['volume_24h']


    print(str(rank) + ': ' + name + ' {' + symbol + '}')
    print(f'circulating supply: {circulating_supply}')
    print(f'total supply: {total_supply}')

    print(f'market cap: {market_cap}')
    print(f'% change in last hour: {percent_change_1h}%')
    print(f'% change in last 24h: {percent_change_24h}%')
    print(f'% change in last week: {percent_change_7d}%')

    print(f'current price: {price}')

    print(f'vol. in last 24h: {volume_24h}')

    print('\n') # new line separator
