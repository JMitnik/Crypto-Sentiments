import re
from collections import defaultdict
import nltk
from NRC import *

REGEX_DAY_PATTERN = '(.*)T'
REGEX_TIME_PATTERN = ''
DAY_STRING = "day"
emo = EmotionModel("test.p", lexicon="lexicon.txt")

def split_tweets_by_day(tweets):
    days = []

    # date_obj = defaultdict(list)

    for tweet in tweets:
        date = re.search(REGEX_DAY_PATTERN, tweet['date']).group(1)

        index = None
        for (key, value) in enumerate(days):
            if value['date'] == date:
                index = key

        if index != None:
            days[index]['tweets'].append(tweet)
        else:
            days.append({
                'date': date,
                'tweets': [tweet]
            })

    return days

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

def get_freq_distr_for_tweets(tweets):
    regular_words = []

    for i in tweets:
        words = i['content'].split(' ')
        for j in words:
            regular_words.append(j)

    fdist = nltk.FreqDist(regular_words)

    for word in sorted(fdist):
        print(word, '->', fdist[word], end='; ')

    return sorted(fdist)
