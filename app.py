from flask import Flask, jsonify, request
from analytics import article_analytics, article_fetcher, tag_analytics

app = Flask(__name__)


@app.route('/')
def hello_world():
    api_key = request.args.get('apiKey', default="", type=str)
    articles = article_fetcher.get_articles_from_dev(api_key)
    tags = tag_analytics.get_tags_from_articles(articles)
    response = jsonify(article_analytics=article_analytics.analyse(articles),
                       tag_analytics=tag_analytics.analyze(tags))

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run()

