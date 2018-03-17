#%%
import CreateDataService
import ReadDataService
import ProcessDataService

regular_tweets = ReadDataService.read_data('1000', 'regular-tweets.csv')
bitcoin_tweets = ReadDataService.read_data('1000', 'bitcoin-tweets.csv')
print(ProcessDataService.get_freq_distr_for_tweets(regular_tweets))

# bitcoin_days = ProcessDataService.split_tweets_by_day(bitcoin_tweets)

CreateDataService.writeDayScoreToCSV('bitcoin-days.csv', bitcoin_days)
