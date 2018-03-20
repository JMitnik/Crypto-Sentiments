#%%
# import CreateDataService
import ReadDataService
import ProcessDataService

# import BitcoinService

# DATA_SOURCE = "sm"

import pandas as pd
import datetime
import re

# try:
#     regular_tweets = ReadDataService.read_data('sm', 'regular-tweets.csv')
#     bitcoin_tweets = ReadDataService.read_data('sm', 'bitcoin-tweets.csv')
# except OSError:
#     print("Create some data first! Use the create_data.py app")
#     raise

# bitcoin_days = ProcessDataService.get_sentiments_by_days(bitcoin_tweets)
# CreateDataService.writeDayScoreToCSV('sentiment-bitcoin-days.csv', DATA_SOURCE, bitcoin_days)

#%%
# values = pd.read_csv('data/2017-10-01:2018-02-02/bitcoin-tweets.csv')
# sorted_coins = ProcessDataService.sort_dataframe_by_date(values)
# sorted_coins.to_csv('data/2017-10-01:2018-02-02/bitcoin-tweets-v2.csv')

bt_tweets = ReadDataService.read_data('2017-10-01-2018-02-02', 'bitcoin-tweets-v2.csv')
print(ProcessDataService.split_tweets_by_day(bt_tweets))
