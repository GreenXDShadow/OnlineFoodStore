from app import db
from Product import Product

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

class Customer(User):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    address = db.Column(db.String)

    # Payment information fields
    card_number_last4 = db.Column(db.String(4))  # Last 4 digits of the card
    expiration_month = db.Column(db.String(2))  # MM format
    expiration_year = db.Column(db.String(4))  # YYYY format

    # Relationship to represent the cart
    cart = db.relationship('Cart', backref='customer', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, email={self.email}, address={self.address})>"

class Manager(User):
    __tablename__ = 'manager'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'manager',
    }

    def __repr__(self):
        return f"<Manager(id={self.id}, name={self.name}, email={self.email})>"

class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    # Relationship to access product details
    product = db.relationship('Product')

    def __repr__(self):
        return f"<Cart(id={self.id}, customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity})>"

