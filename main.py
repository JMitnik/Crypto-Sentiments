#%%
import twin_nl as TweetService
import nltk
import csv
from NRC import *


emo = EmotionModel("test.p", lexicon="lexicon.txt")
print(emo.predict("Wat ben ik blij."))

regular_tweets = TweetService.get_tweets(
    "2018-01-01T22:10:00.000Z",
    "2018-02-02T23:20:00.000Z",
    10000,
    'een,het,de'
)

bitcoin_tweets = TweetService.get_tweets(
    "2018-01-01T22:10:00.000Z",
    "2018-02-02T23:20:00.000Z",
    10000,
    'bitcoin'
)

#%%
def sum_sentiment_scores(days):
    for (index, day) in enumerate(days):
        pos = 0
        neg = 0

        for tweet in day['tweets']:
            content = tweet['content'][0]
            sentiments = emo.predict(content)['sentiment']

            if sentiments['negative'] > sentiments['positive']:
                pos+=1
            else:
                neg+=1

        day['sentiment'] = {
            'positive': pos,
            'negative': neg
        }

        days[index] = day
    return days

bitcoin_days = sum_sentiment_scores(TweetService.split_tweets_by_day(bitcoin_tweets))

#%%

def writeTweetSourceToCsv(file_name, tweets):
    with open(file_name, 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for tweet in regular_tweets:
            print(tweet)
            writer.writerow([tweet['date'], tweet['content'][0], tweet['author']])

def writeDayScoreToCSV(file_name, days):
    with open(file_name, 'w', encoding="utf-8") as file:
        writer = csv.writer(file)

        for day in days:
            writer.writerow([day['date'], day['sentiment']['positive'], day['sentiment']['negative']])

writeDayScoreToCSV('bitcoin-days.csv', bitcoin_days)
writeTweetSourceToCsv('regular-tweets.csv', regular_tweets)
writeTweetSourceToCsv('bitcoin-tweets.csv', bitcoin_tweets)

#%%
regular_words = []

for i in regular_tweets:
    words = i['content'][0].split(' ')
    for j in words:
        regular_words.append(j)

fdist = nltk.FreqDist(regular_words)

for word in sorted(fdist):
    print(word, '->', fdist[word], end='; ')


print(regular_tweets)
# scores_by_unit = ScoreService.calculate_average_sentiment_scores(tweets)
