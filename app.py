from flask import Flask, jsonify, make_response
import twin_nl as TweetService

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello!"

@app.route("/tweets")
def tweets():
      print("Get tweets")
      tweets = TweetService.get_tweets(
          "2017-06-09T23:10:00.000Z", "2017-06-11T23:20:00.000Z", 'bitcoin' 1)
      return jsonify(tweets)

if __name__ == "__main__":
  app.run()
