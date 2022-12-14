from flask import Flask
import apis

app = Flask(__name__)


@app.route("/")
def home():
    return apis.fullData


if __name__ == "__main__":
    app.run(debug=True)
