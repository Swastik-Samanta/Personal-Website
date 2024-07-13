from flask import Flask, render_template, request, jsonify
from chat import get_response

application = Flask(__name__)


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
    application.run(host='0.0.0.0', port=5000, debug=True)