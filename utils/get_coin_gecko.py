from pycoingecko import CoinGeckoAPI
from datetime import datetime
import time
import pandas as pd


def modify_gecko_output(output, amount, crypto):
    to_df = pd.DataFrame.from_dict(output['prices'])
    to_df.columns = ['Date', 'Price']
    to_df['Date'] = pd.to_datetime(to_df['Date'], unit='ms')
    to_df['Price'] = to_df['Price'].astype(float).apply(lambda x: x * amount)
    to_df['Crypto'] = crypto
    return to_df


def get_prices(crypto, from_date, amount):
    cg = CoinGeckoAPI()
    df = []

    for index, (c, d, a) in enumerate(zip(crypto, from_date, amount)):
        output = cg.get_coin_market_chart_range_by_id(id=c,
                                                      vs_currency='eur',
                                                      from_timestamp=str(time.mktime(datetime.strptime(d, "%d/%m/%Y").timetuple())),
                                                      to_timestamp=str(time.mktime(datetime.now().timetuple())))
        df.append(modify_gecko_output(output, a, c))

    return pd.concat(df)


# def get_available_currencies():
#     return [element['id'] for element in cg.get_coins_list()]
