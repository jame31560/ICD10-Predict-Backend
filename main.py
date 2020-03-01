from flask import Flask
from flask import jsonify, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"hello": "world"})


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
