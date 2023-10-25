from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return "Hello!"


app.run("0.0.0.0", debug=True, port=5050)
