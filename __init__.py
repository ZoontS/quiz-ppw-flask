from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def create_app():
    return render_template("index.html")
