from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
  # do something with the request data
  return render_template('index.html', name= index)

