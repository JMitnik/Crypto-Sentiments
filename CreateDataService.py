import twin_nl as TweetService
import csv

def createData(start_date, end_date, nr,source):
    regular_tweets = TweetService.get_tweets(
        start_date,
        end_date,
        nr,
        'een,het,de'
    )

    bitcoin_tweets = TweetService.get_tweets(
       start_date,
        end_date,
        nr,
        'bitcoin'
    )

    _writeTweetSourceToCsv('data/'+source+'/regular-tweets.csv', regular_tweets)
    _writeTweetSourceToCsv('data/'+source+'/bitcoin-tweets.csv', bitcoin_tweets)


def _writeTweetSourceToCsv(file_name, tweets):
    with open(file_name, 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for tweet in tweets:
            print(tweet)
            writer.writerow(
                [tweet['date'], tweet['content'][0], tweet['author']])

def writeDayScoreToCSV(file_name, days):
    with open(file_name, 'w', encoding="utf-8") as file:
        writer = csv.writer(file)

        for day in days:
            writer.writerow([day['date'], day['sentiment']['positive'], day['sentiment']['negative']])
