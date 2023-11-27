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
app.config['UPLOAD_FOLDER'] = 'static\Icons'  # Add this line


db = SQLAlchemy(app)

# Importing the models
from Product import Product
from User import User, Customer, Manager, Cart
from flask import Flask, render_template, request, redirect, session
from sqlalchemy.exc import IntegrityError

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)

with app.app_context():
    db.create_all()

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

    @staticmethod
    @app.route('/api/login', methods=['POST'])
    def login():
        name = request.form.get('userName')
        password = request.form.get('passWord')

        user = db.session.query(User).filter(User.name == name, User.password == password, ).first()

        if not user:
            return jsonify({"status": "error", "message": "Failed to log in"})
        else:
            session['logged_in'] = True
            session['username'] = user.name
            session['user_id'] = user.id
            return render_template('index.html', session = session)

    @staticmethod
    @app.route('/api/logout', methods =['POST'])
    def logout():
        if 'logged_in' in session:
            session.pop('logged_in', None)
            session.pop('username', None)
            session.pop('user_id', None)
        return render_template('index.html', session=session)

    @staticmethod
    @app.route('/api/addToCart', methods = ['POST'])
    def addToCart():
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        user_id = session.get('user_id')
        cart_item = Cart.query.filter_by(product_id=product_id, customer_id=user_id).first()
        if cart_item:
            # If the product is already in the cart, update the quantity
            cart_item.quantity += int(quantity)
        else:
            # If the product is not in the cart, create a new cart item
            cart_item = Cart(product_id=product_id, customer_id=user_id, quantity=int(quantity))
            db.session.add(cart_item)

        db.session.commit()
        return jsonify({"status": "success", "message": "Item added successfully"})

    @staticmethod
    @app.route('/api/removeFromCart', methods=['POST'])
    def removeFromCart():
        product_id = request.form.get('product_id')
        user_id = session.get('user_id')

        if not user_id:
            return jsonify({"status": "error", "message": "User not logged in"})

        cart_item = Cart.query.filter_by(product_id=product_id, user_id=user_id).first()

        if cart_item:
            # If the product is found in the cart, remove it
            db.session.delete(cart_item)
            db.session.commit()
            #return jsonify({"status": "success", "message": "Product removed from cart successfully"})
        else:
            return jsonify({"status": "error", "message": "Product is not in the cart"})

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
    dairy_products = Product.query.filter_by(category='dairy').all()  # Replace with your actual query
    return render_template('dairy.html', products=dairy_products)

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

@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/cart')
def cart():
    if 'user_id' not in session:
        # Redirect to login page or show a message that user is not logged in
        return redirect(url_for('login'))

    user_id = session['user_id']
    cart_items = Cart.query.filter_by(customer_id=user_id).all()

    subtotal = 0
    for item in cart_items:
        product = Product.query.get(item.product_id)
        subtotal += product.price * item.quantity

    shipping_cost = 0.15 * subtotal if subtotal > 20 else 0

    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal, shipping_cost=shipping_cost)

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    user_id = session.get('user_id')
    if not user_id:
        # Handle not logged in case
        return redirect(url_for('login'))

    quantity_to_remove = int(request.form.get('quantity_to_remove'))
    cart_item = Cart.query.filter_by(customer_id=user_id, product_id=product_id).first()

    if cart_item:
        if cart_item.quantity > quantity_to_remove:
            cart_item.quantity -= quantity_to_remove
        else:
            db.session.delete(cart_item)
        db.session.commit()
        flash('Item removed successfully')

    return redirect(url_for('cart'))


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/featured')
def featured():
    return render_template('featured.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'myFile[]' not in request.files:
            return 'No file part'

        files = request.files.getlist('myFile[]')

        for file in files:
            if file.filename == '':
                return 'No selected file'

            # Save the file to the specified folder
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            # Insert file info into the database using SQLAlchemy
            new_upload = Upload(filename=file.filename)
            db.session.add(new_upload)
            db.session.commit()

        return 'File(s) uploaded successfully'

    return render_template('upload.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run(debug=True)
