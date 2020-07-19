from flask import Flask, request, render_template, url_for, session, redirect
import json

app = Flask(__name__)


@app.route("/")
def show_promotions():
    return render_template("home.html")


app.run(debug=True)
