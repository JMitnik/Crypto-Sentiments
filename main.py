#%%
import CreateDataService
import ReadDataService
import ProcessDataService

import BitcoinService

DATA_SOURCE = "sm"

try:
    regular_tweets = ReadDataService.read_data('sm', 'regular-tweets.csv')
    bitcoin_tweets = ReadDataService.read_data('sm', 'bitcoin-tweets.csv')
except OSError:
    print("Create some data first! Use the create_data.py app")
    raise

bitcoin_days = ProcessDataService.get_sentiments_by_days(bitcoin_tweets)
CreateDataService.writeDayScoreToCSV('sentiment-bitcoin-days.csv', DATA_SOURCE, bitcoin_days)
