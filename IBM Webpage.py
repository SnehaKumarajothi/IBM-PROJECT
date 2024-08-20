from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/test")
def test():
    return render_template('test.html')
