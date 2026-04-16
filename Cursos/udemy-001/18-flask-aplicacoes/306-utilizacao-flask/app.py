from flask import Flask

app = Flask(__name__)


@app.route("/")
def principal():
    return "Hello World"


# flask flask --app app run
# flask flask --app app run --debug
