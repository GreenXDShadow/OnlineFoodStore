import os
from flask import Flask, jsonify, flash, redirect, render_template, request, url_for, jsonify, make_response

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

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
from User import User, Customer, Manager, Cart, Order
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
            flash("User added successfully", "success")  # 'success' is a category
            return redirect(url_for('userlogin'))  # Redirect to the form page
        except IntegrityError:
            flash("Email already exists", "error")  # Using flash for error message
            return redirect(url_for('userlogin'))  # Redirect back to the form
        except Exception as e:
            flash("An error occurred. Please try again.", "error")
            return redirect(url_for('userlogin'))

    @app.route('/api/login', methods=['POST'])
    def login():
        name = request.form.get('userName')
        password = request.form.get('passWord')

        user = db.session.query(User).filter(User.name == name, User.password == password).first()

        if not user:
            flash("Signup unsuccessful. Please try again.", "error")
            if session['user_type'] == 'customer':
                return redirect(url_for('userlogin'))
            else:
                return redirect(url_for('adminlogin'))
        else:
            session['logged_in'] = True
            session['username'] = user.name
            session['user_id'] = user.id
            session['user_type'] = user.type
            return render_template('index.html', session=session)

    @staticmethod
    @app.route('/api/logout', methods =['POST'])
    def logout():
        if 'logged_in' in session:
            session.pop('logged_in', None)
            session.pop('username', None)
            session.pop('user_id', None)
        return render_template('index.html', session=session)

    @app.route('/api/addToCart', methods=['POST'])
    def addToCart():
        product_id = request.form.get('product_id')
        user_id = session.get('user_id')

        if not user_id:
            return jsonify({"status": "error", "message": "User not logged in"})

        product = Product.query.get(product_id)
        if not product:
            return jsonify({"status": "error", "message": "Product not found"})

        cart_item = Cart.query.filter_by(product_id=product_id, customer_id=user_id).first()
        quantity = int(request.form.get('quantity', 1))
        if product.quantity < quantity:
            return jsonify({"status": "failed", "message": "Not enough stock"})

        if product.type == 'fresh':
            weight = float(request.form.get('weight', 0))
            total_price = product.price * weight

            if cart_item:
                # Update weight and price for existing cart item
                cart_item.quantity += weight
                product.quantity -= weight
                cart_item.total_price += total_price
            else:
                # Create a new cart item for fresh product
                cart_item = Cart(product_id=product_id, customer_id=user_id, quantity=weight, total_price=total_price)
                product.quantity -= weight
                db.session.add(cart_item)
        else:
            # Logic for packaged products remains the same
            quantity = int(request.form.get('quantity', 1))
            if cart_item:
                cart_item.quantity += quantity
                product.quantity -= quantity
            else:
                cart_item = Cart(product_id=product_id, customer_id=user_id, quantity=quantity)
                product.quantity -= quantity
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
    fruit_products = Product.query.filter_by(category='fruit').all()  # Replace with your actual query
    return render_template('fruit.html', products=fruit_products)


@app.route('/vegetable')
def vegetable():
    return render_template('vegetable.html')


@app.route('/dairy')
def dairy():
    dairy_products = Product.query.filter_by(category='dairy').all()  # Replace with your actual query
    return render_template('dairy.html', products=dairy_products)

@app.route('/meat')
def meat():
    meat_products = Product.query.filter_by(category='meat').all()  # Replace with your actual query
    return render_template('meat.html', products=meat_products)


@app.route('/frozen') #frozen_food_products
def frozen():
    frozen_food_products = Product.query.filter_by(category='frozen').all()  # Replace with your actual query
    return render_template('frozen.html', products=frozen_food_products)


@app.route('/beverages')
def beverages():
    beverage_products = Product.query.filter_by(category='beverages').all()  # Replace with your actual query
    return render_template('beverages.html', products=beverage_products)


@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        weight = float(request.form.get('weight', 0))

        # Collecting values from checkboxes for type and category
        type_list = request.form.getlist('type')
        category_list = request.form.getlist('category')

        # Convert list to comma-separated string
        type_ = ', '.join(type_list)
        category = ', '.join(category_list)

        quantity = int(request.form.get('quantity', 0))
        amount = float(request.form.get('amount', 0))

        # Handling file upload for image path
        file = request.files['imagePath']
        file_path = ''  # Default empty file path
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file_path = 'Icons/' + filename  # Modified file path
            full_path = os.path.join(app.root_path, 'static', file_path)  # Full path for saving the file
            file.save(full_path)  # Saving the file to the filesystem

        # Create a new Product instance
        new_product = Product(
            name=name, price=price, weight=weight, type=type_,
            category=category, quantity=quantity, amount=amount, imagePath=file_path
        )

        # Adding the new product to the database
        db.session.add(new_product)
        db.session.commit()

        # Show a confirmation message
        flash('Product added successfully!')

        # Redirect to some page after adding
        return redirect(url_for('index'))

@app.route('/cart')
def cart():
    if 'user_id' not in session:
        flash('You need to log in first', 'info')  # 'info' is the category of the message
        return redirect(url_for('index'))  # Redirect to homepage or login page

    user_id = session['user_id']
    cart_items = Cart.query.filter_by(customer_id=user_id).all()

    subtotal = 0
    for item in cart_items:
        product = Product.query.get(item.product_id)
        subtotal += product.price * item.quantity

    sales_tax = 0.03 * subtotal  # 3% sales tax
    shipping_cost = 0.15 * subtotal if subtotal > 20 else 0
    grand_total = subtotal + sales_tax + shipping_cost

    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal, sales_tax=sales_tax, shipping_cost=shipping_cost, grand_total=grand_total)


@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    user_id = session.get('user_id')
    if not user_id:
        # Handle not logged in case
        return redirect(url_for('login'))

    quantity_to_remove = float(request.form.get('quantity_to_remove'))
    quantity_to_remove = round(quantity_to_remove, 2)
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
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    cart_items = Cart.query.filter_by(customer_id=user_id).all()

    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    sales_tax = subtotal * 0.03  # Assuming 3% sales tax
    shipping_cost = 5.00 if subtotal > 20 else 0
    grand_total = subtotal + sales_tax + shipping_cost

    return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal, sales_tax=sales_tax, shipping_cost=shipping_cost, grand_total=grand_total)

@app.route('/api/updateUser', methods=['POST'])
def updateUser():
    # Assuming user_id is stored in session when the user logs in
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({"status": "error", "message": "User not logged in"})

    # Retrieve user from database
    user = User.query.get(user_id)

    if not user:
        return jsonify({"status": "error", "message": "User not found"})

    # Update user fields from form data
    user.delivery_first_name = request.form.get('firstname')
    user.delivery_last_name = request.form.get('lastname')
    user.delivery_address1 = request.form.get('address1')
    user.delivery_address2 = request.form.get('address2')
    user.delivery_city = request.form.get('city')
    user.delivery_state = request.form.get('state')
    user.delivery_zipcode = request.form.get('zipcode')
    # Update payment information
    user.billing_address = request.form.get('billing_address')
    user.card_number = request.form.get('card_number')
    user.card_expiration_date = request.form.get('card_expiration_date')
    user.card_cvv = request.form.get('card_cvv')

    # Save changes
    try:
        db.session.commit()
        return jsonify({"status": "success", "message": "User updated successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": "Error updating user: " + str(e)})

@app.route('/api/submitOrder', methods=['POST'])
def submitOrder():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"status": "error", "message": "User not logged in"})

    user = User.query.get(user_id)
    if not user:
        return jsonify({"status": "error", "message": "User not found"})

    # Check if delivery and payment information is complete
    if not all([user.delivery_first_name, user.delivery_last_name, user.delivery_address1,
               user.delivery_city, user.delivery_state, user.delivery_zipcode,
               user.billing_address, user.card_number, user.card_expiration_date, user.card_cvv]):
        return jsonify({"status": "error", "message": "Please fill out all delivery and payment information"})

    # Here you would normally add logic to process the payment
    # For simplicity, we'll skip this step
    cart_items = Cart.query.filter_by(customer_id=user_id).all()

    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    sales_tax = subtotal * 0.03  # Assuming 3% sales tax
    shipping_cost = 5.00 if subtotal > 20 else 0
    grand_total = subtotal + sales_tax + shipping_cost

    new_order = Order(customer_id=user_id, total_price=grand_total)
    db.session.add(new_order)

    # Clear the user's cart
    Cart.query.filter_by(customer_id=user_id).delete()
    db.session.commit()

    return jsonify({"status": "success", "message": "Thank you for your order"})

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

@app.route('/api/addManager', methods=['POST'])
def addManager():
    master_key = request.form.get('masterKey')

    if master_key != '54321':
        flash("Invalid Masterkey", "error")
        return redirect(url_for('adminlogin'))    
    
    name = request.form.get('name')
    password = request.form.get('password')
    email = request.form.get('email')

    if not all([name, password, email]):
        flash("All fields must be filled out", "error")
        return redirect(url_for('adminlogin'))

    try:
        new_manager = Manager(name=name, password=password, email=email)
        db.session.add(new_manager)
        db.session.commit()
        flash("Admin added successfully", "success")
        return redirect(url_for('adminlogin'))
    except IntegrityError:
        flash("Email already exists", "error")
        return redirect(url_for('adminlogin'))


@app.route('/api/loginManager', methods=['POST'])
def loginManager():
    email = request.form.get('email')
    password = request.form.get('password')

    manager = Manager.query.filter_by(email=email, password=password).first()

    if manager:
        session['username'] = manager.name
        session['user_id'] = manager.id
        session['user_type'] = 'admin'  # Set user type as admin
        return redirect(url_for('index'))
    else:
        flash("Invalid email or password", "error")  # Use the flash function here
        return redirect(url_for('adminlogin'))  # Redirect to the admin login page
    
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    results = Product.query.filter(
        (Product.name.ilike(f"%{query}%")) |
        (Product.category.ilike(f"{query}"))
    ).all()

    return render_template('search_results.html', search_results=results, query=query)
@app.route('/change_stock', methods=['GET'])
def change_stock_form():
    # Fetch all products to populate the dropdown
    products = Product.query.all()
    return render_template('upload.html', products=products)

@app.route('/change_stock', methods=['POST'])
def change_stock():
    product_id = request.form.get('product_id')
    new_quantity = request.form.get('quantity')
    print(new_quantity)

    # Logic to update the stock quantity for the selected product
    product = Product.query.get(product_id)
    print(product)
    if product:
        product.quantity = new_quantity
        db.session.commit()
        flash('Stock quantity updated successfully', 'success')
    else:
        flash('Product not found', 'error')

    return redirect(url_for('change_stock_form'))




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run(debug=True)
