import requests, json
import config

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}
request = requests.get(listings_url, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

# print(results)

for currency in results['data']: 
    # print(currency)
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + ' {' + symbol + '}')