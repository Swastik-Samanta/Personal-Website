from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

application = Flask(__name__)
CORS(application)


@application.get("/")
def index_get():
    return render_template("index.html")

@application.post("/predict")
def predict():
    text = request.get_json().get("message")
    # Check if text is valid.
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    application.run(debug=True)