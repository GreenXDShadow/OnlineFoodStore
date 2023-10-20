from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fruit')
def fruit():
    return render_template('fruit.html')

@app.route('/vegetable')
def vegetable():
    return render_template('vegetable.html')

@app.route('/dairy')
def dairy():
    return render_template('dairy.html')

@app.route('/meat')
def meat():
    return render_template('meat.html')

@app.route('/frozen')
def frozen():
    return render_template('frozen.html')

@app.route('/beverages')
def beverages():
    return render_template('beverages.html')

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')
