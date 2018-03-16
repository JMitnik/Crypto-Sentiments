#%%
import twin_nl as TweetService
import nltk
import csv
# import scorer as ScoreService
# import crypto as CryptoService

# bitcoin_tweets = TweetService.get_tweets(
#     "2017-06-10T22:10:00.000Z",
#     "2017-06-11T23:20:00.000Z",
#     10,
#     'bitcoin'
# )

regular_tweets = TweetService.get_tweets(
    "2017-06-10T22:10:00.000Z",
    "2017-06-11T23:20:00.000Z",
    10,
    'een,het,de'
)

#%%
def writeTweetSourceToCsv(file_name, tweets):
    with open(file_name, 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for tweet in regular_tweets:
            writer.writerow([tweet['date'], tweet['content'][0], tweet['author']])

writeTweetSourceToCsv('test-tweets.csv', regular_tweets)

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
