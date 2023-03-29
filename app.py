from flask import Flask, render_template, request

from helpers import login_required

# Configure application
app = Flask(__name__)

@app.route("/")
@login_required
def index():
    return render_template("apology.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template("apology.html")
    else:
        return render_template("login.html")

