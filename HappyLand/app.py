
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/explore")
def explore():
    return render_template("explore.html")


@app.route("/act")
def act():
    return render_template("act.html")


if __name__ == "__main__":
    app.run(debug=True)
