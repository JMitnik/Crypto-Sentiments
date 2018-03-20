#%%
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import numpy as np
import re

REGEX_DAY_PATTERN = '(.*)T'

importUrl = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start={}&end={}"

def get_bitcoin_values(start_date, end_date):
    url = importUrl.format(start_date, end_date)
    bitcoinMarketInfo = pd.read_html(url)[0]

    bitcoinMarketInfo = bitcoinMarketInfo.assign(Date=pd.to_datetime(bitcoinMarketInfo['Date']))
    bitcoinMarketInfo['Volume'] = bitcoinMarketInfo['Volume'].astype('int64')
    kwargs = {'day_diff': lambda x: (x['Close'] - x['Open']) / x['Open']}
    bitcoinMarketInfo = bitcoinMarketInfo.assign(**kwargs)
    print(bitcoinMarketInfo.head())

    return bitcoinMarketInfo

def get_coinmarketcap_date_range(start_date, end_date):
    start_date_plain = re.search(REGEX_DAY_PATTERN, start_date).group(1)
    end_date_plain = re.search(REGEX_DAY_PATTERN, end_date).group(1)

    start_date_object = time.strptime(start_date_plain, '%Y-%m-%d')
    end_date_object = time.strptime(end_date_plain, '%Y-%m-%d')

    coinmarketcap_start_date = time.strftime('%Y%m%d', start_date_object)
    coinmarketcap_end_date = time.strftime('%Y%m%d', end_date_object)

    return (coinmarketcap_start_date, coinmarketcap_end_date)
