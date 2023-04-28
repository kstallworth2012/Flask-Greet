from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/welcome")
def welcome():
    """
    /welcome
    Returns “welcome”
    """
    return "<h1>Welcome</h1>"

@app.route("/welcome/home")
def home():
    """
    /welcome/home
    Returns “welcome home”
    """
    return "<h1>Welcome Home</h1>"

@app.route("/welcome/back")
def welcome_back():
    """
    /welcome/back
    Return “welcome back”
    """
    return "<h1>Welcome back</h1>"