import json, requests
import config

global_url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest"

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_KEY,
}

params = {
    'convert': 'GBP'
}

request = requests.get(global_url, headers=headers, params=params)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

active_cryptocurrencies = results['data']['active_cryptocurrencies']
active_market_pairs = results['data']['active_market_pairs']
btc_dominance = results['data']['btc_dominance']
eth_dominance = results['data']['eth_dominance']
last_updated = results['data']['last_updated']
defi_market_cap = results['data']['defi_market_cap']
derivatives_volume_24h = results['data']['derivatives_volume_24h']