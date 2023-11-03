import os
from flask import Flask, jsonify, flash, redirect, render_template, request, url_for, jsonify

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Update this key (placeholder for now)
app.secret_key = 'your_secret_key_here'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importing the models
from Product import Product, BoxedProduct, FreshProduct
from User import User, Customer, Manager, Cart

from sqlalchemy.exc import IntegrityError

class ApiCalls:
    @staticmethod
    @app.route('/api/addUser', methods=['POST'])
    def addUser():
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        confirm_password = request.form.get('confirm_password')

        # Check if any field is empty
        if not all([name, password, email, confirm_password]):
            return jsonify({"status": "error", "message": "All fields must be filled out"})

        # Check password confirmation
        if password != confirm_password:
            return jsonify({"status": "error", "message": "Passwords do not match"})

        # Attempt to add user to database
        try:
            new_user = Customer(name=name, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"status": "success", "message": "User added successfully"})
        except IntegrityError:  # This is for the unique constraint error
            return jsonify({"status": "error", "message": "Email already exists"})
        except Exception as e:
            # Handle other database exceptions here
            return jsonify({"status": "error", "message": "An error occurred while registering. Please try again."})



# These app routes are 'URL' requests. A function will be run whenever the web page reaches any of these URLs.
@app.route('/')
def index():
    # blank for now, will accept login/ registration form info soon
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


@app.route('/cart')
def cart():
    # if user is logged in we will display the items in their current cart here with a total
    return render_template('cart.html')

if __name__ == "__main__":
    app.run(debug=True)
