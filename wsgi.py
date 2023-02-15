from flask import Flask, render_template, redirect

app = Flask(__name__, )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bingus")
def bingus():
    return render_template("bingus/index.html")


@app.route("/courses")
def courses():
    return redirect("https://vandad.notion.site/5f1c9a2621224ac584fda9a8a5ade9d1?v=791d53f5a37849409712e6489ec41689")
