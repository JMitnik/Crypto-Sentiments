import urllib.request
import json
import re
from urllib import request
from bs4 import BeautifulSoup
from collections import defaultdict

REGEX_DAY_PATTERN = '(.*)T'
REGEX_TIME_PATTERN = ''
DAY_STRING = "day"
TWINL_QUERY_URI = "https://twinl.surfsara.nl/api/search/ids?start={}&end={}&query={}&casesensitive=false&startfrom=0&size={}"
TWINL_URI = "https://twinl.surfsara.nl/api/search/ids?start={}&end={}&casesensitive=false&startfrom=0&size={}"
TWITTER_API_URL = "https://twitter.com/{}/status/{}"

def get_tweets(start_date, end_date, max_tweet_nr, query=None):
    if query != None:
        url = TWINL_QUERY_URI.format(start_date, end_date, query, max_tweet_nr)
    else:
        url = TWINL_URI.format(start_date, end_date, max_tweet_nr)

    meta_tweets = __fetch_meta_tweets(url)
    tweets = __get_meta_tweets_contents(meta_tweets)
    return tweets

def get_tweets_by_date(start_date, end_date, max_tweet_nr, query=None):
    tweets = get_tweets(start_date, end_date, max_tweet_nr, query)
    return __split_tweets_by(tweets, DAY_STRING)

def __fetch_meta_tweets(url):
    twinlNl_JSON = urllib.request.urlopen(url)
    return json.loads(twinlNl_JSON.read().decode('utf-8'))['tweets']

def __get_meta_tweets_contents(meta_tweets):
    result = []

    for meta_tweet in meta_tweets:
        meta_data = meta_tweet['fields']
        url = TWITTER_API_URL.format(meta_data['userid'][0], meta_data['id'][0])

        try:
            tweet_content = __get_tweet_content(url)

            if tweet_content:
                result.append({
                    'author': meta_data['username'][0],
                    'content': tweet_content,
                    'date': meta_data['timestamp'][0]
                })
        except:
            print(url)

    return result

def __get_tweet_content(url):
    try:
        html = request.urlopen(url).read().decode('utf8')
        raw = BeautifulSoup(html, 'html.parser')
        return [i.get_text() for i in raw.find_all("p", class_="tweet-text")]
    except:
        return None

def __split_tweets_by(tweets, split_date):
    if split_date == DAY_STRING:
        return split_tweets_by_day(tweets)

def split_tweets_by_day(tweets):
    days = []

    # date_obj = defaultdict(list)

    for tweet in tweets:
        date = re.search(REGEX_DAY_PATTERN, tweet['date']).group(1)

        index = None
        for (key, value) in enumerate(days):
            if value['date'] == date:
                index = key
        # index = [key if value.date == date for (key, value) in enumerate(days, 0)][0]

        if index != None:
            days[index]['tweets'].append(tweet)
        else:
            days.append({
                'date':date,
                'tweets':[tweet]
            })

        # date_obj[date].append(tweet)
    return days

    # return date_obj



# This splits the tweets by date
