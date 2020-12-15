from flask import Flask, jsonify, request
from analytics import article_analytics, article_fetcher

app = Flask(__name__)


@app.route('/')
def hello_world():
    api_key = request.args.get('apiKey', default="", type=str)
    articles = article_fetcher.get_articles_from_dev(api_key)
    response = jsonify(article_analytics.analyse(articles))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run()

