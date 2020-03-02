from flask import Flask
from flask import jsonify, request


app = Flask(__name__)


@app.route("/api/predict", methods=["POST"])
def hello_world():
    request_data = request.json
    if "pre_data" in request_data:
        try:
            """
            Call your predict function
            Recommended to import the function to use.
            """
            return jsonify({
                "status": "Success",
                "data": [
                    {
                        "title": "糖尿病",
                        "code": "456.78",
                        "probability": 0.9766,
                        "mark": True
                    },
                    {
                        "title": "心臟病",
                        "code": "878.87",
                        "probability": 0.1256,
                        "mark": False
                    }
                ]
            }), 200
        except:
            return jsonify({
                "status": "Error",
                "description": "Server Error."
            }), 500
    else:
        return jsonify({
            "status": "Error",
            "description": "Error parameter."
        }), 400


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
