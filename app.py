from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello__world(): 
    return "hello world"