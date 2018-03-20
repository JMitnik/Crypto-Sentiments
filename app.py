from flask import Flask, jsonify, make_response, request
import twin_nl as TweetService
import BitcoinService

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello!"

@app.route('/date/months')
def get_results_for_months():
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    print(start_date, end_date)
    btc = BitcoinService.get_bitcoin_values(
        start_date, end_date).to_dict('records')
    return jsonify(result=btc)

# @app.route("/tweets")
# def tweets():
#       print("Get tweets")
#       tweets = TweetService.get_tweets(
#           "2017-06-09T23:10:00.000Z", "2017-06-11T23:20:00.000Z", 'bitcoin' 1)
#       return jsonify(tweets)

if __name__ == "__main__":
  app.run()
