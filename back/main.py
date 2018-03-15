import twin_nl as TweetService
# import scorer as ScoreService
# import crypto as CryptoService

tweets = TweetService.get_tweets(
    "2017-06-10T22:10:00.000Z",
    "2017-06-11T23:20:00.000Z",
    10
)

print(tweets)
# scores_by_unit = ScoreService.calculate_average_sentiment_scores(tweets)
