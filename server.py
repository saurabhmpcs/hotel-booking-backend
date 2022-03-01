from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login")
def login():
    return "<p>LOGIN</p>"

@app.route("/signup")
def signup():
    return "<p>signup</p>"