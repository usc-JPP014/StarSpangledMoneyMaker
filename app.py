from backend import Year
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    my_string = "Please enter a year between 2017 and 2066"
    return render_template("index.html", body=my_string)


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    y = Year(text)
    return y.run()


if __name__ == "__main__":
    app.run()

