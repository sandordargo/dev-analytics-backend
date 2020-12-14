from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    response = jsonify(message='Hello World, this is DEV analytics here!')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run()

