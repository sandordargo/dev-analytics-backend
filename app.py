from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    api_key = request.args.get('apiKey', default="", type=str)
    response = jsonify(message=f'Hello {api_key}, this is DEV analytics here!')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run()

