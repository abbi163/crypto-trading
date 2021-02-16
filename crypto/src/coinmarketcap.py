from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import datetime

def cmc():
    '''
    returns all data of coinmarket cap for current date. 
    Note: We are using api so it's very limited ! Save the data . 
    
    '''
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'f900435b-1756-4cfb-8eda-7575d2937c6e',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    #     print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    result = []

    for k in range(0, len(data['data'])):
        id_no =  data['data'][k]['id']
        name = data['data'][k]['name']
        symbol =  data['data'][k]['symbol']
        slug = data['data'][k]['slug']
        num_market_pairs =  data['data'][k]['num_market_pairs']
        date_added = data['data'][k]['date_added']
        tags = data['data'][k]['tags']
        max_supply =  data['data'][k]['max_supply']
        circulating_supply = data['data'][k]['circulating_supply']
        total_supply =  data['data'][k]['total_supply']
        platform = data['data'][k]['platform']
        cmc_rank =  data['data'][k]['cmc_rank']
        last_updated = data['data'][k]['last_updated']
        price = data['data'][k]['quote']['USD']['price']
        volume_24h = data['data'][k]['quote']['USD']['volume_24h']
        percent_change_1h = data['data'][k]['quote']['USD']['percent_change_1h']
        percent_change_24h = data['data'][k]['quote']['USD']['percent_change_24h']
        percent_change_7d = data['data'][k]['quote']['USD']['percent_change_7d']
        market_cap = data['data'][k]['quote']['USD']['market_cap']
        last_updated_quote = data['data'][k]['quote']['USD']['last_updated']

        result.append((
                      id_no, name, symbol, slug,
                      num_market_pairs, date_added, tags, 
                      max_supply, circulating_supply, total_supply, platform,
                      cmc_rank, last_updated, price, volume_24h, percent_change_1h,
                      percent_change_24h, percent_change_7d, market_cap, last_updated_quote
                      ))   
    columns=['id', 'name', 'symbol', 'slug',
             'num_market_pairs', 'date_added', 'tags',
             'max_supply', 'circulating_supply', 'total_supply', 'platform',
             'cmc_rank', 'last_updated', 'price', 'volume_24h', 'percent_change_1h',
             'percent_change_24h', 'percent_change_7d', 'market_cap', 'last_updated_quote']
    dataframe = pd.DataFrame(data=result, columns=columns)
    return dataframe