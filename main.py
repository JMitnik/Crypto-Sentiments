#%%
import CreateDataService
import ReadDataService
import ProcessDataService

regular_tweets = ReadDataService.read_data('sm', 'regular-tweets.csv')

bitcoin_tweets = ReadDataService.read_data('sm', 'bitcoin-tweets.csv')
bitcoin_days = ProcessDataService.split_tweets_by_day(bitcoin_tweets)


writeDayScoreToCSV('bitcoin-days.csv', bitcoin_days)
