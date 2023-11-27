from app import app, db
from User import User, Customer, Manager, Cart
from Product import Product


def clear_tables():
    """
    Clear all data from the tables.
    """
    Cart.query.delete()
    Customer.query.delete()
    Manager.query.delete()
    User.query.delete()
    Product.query.delete()


def populate_data():
    # Populate User, Customer, and Manager
    user1 = User(name="JohnDoe", password="password123", email="johndoe@example.com")
    customer1 = Customer(name="JaneDoe", password="password456", email="janedoe@example.com", address="123 Main St",
                         card_number_last4="1234", expiration_month="12", expiration_year="2025")
    manager1 = Manager(name="AdminUser", password="adminpass", email="admin@example.com")

    db.session.add(user1)
    db.session.add(customer1)
    db.session.add(manager1)


    # Default dairy products
    dairy_products = [
        Product(name="Milk", weight=1.0, type="packaged", category="dairy", imagePath="Icons/milk.png", quantity=1, amount=None),
        Product(name="that Cheese", weight=0.5, type="packaged", category="dairy", imagePath="Icons/cheese.png",quantity=1, amount=None),
        Product(name="Eggsssss", weight=0.6, type="packaged", category="dairy", imagePath="Icons/eggs.png", quantity=1,amount=None),
        Product(name="Almond Milk", weight=1.0, type="packaged", category="dairy", imagePath="Icons/almondmilk.png",quantity=1, amount=None),
        Product(name="Yogurt", weight=0.4, type="packaged", category="dairy", imagePath="Icons/yogurt.png", quantity=1,amount=None),
        Product(name="Butter", weight=0.25, type="packaged", category="dairy", imagePath="Icons/butter.png", quantity=1,amount=None),
        Product(name="Whipped Cream", weight=0.2, type="packaged", category="dairy", imagePath="Icons/whippedcream.png",quantity=1, amount=None),
        Product(name="Soy Milk", weight=1.0, type="packaged", category="dairy", imagePath="Icons/soymilk.png",quantity=1, amount=None)
    ]

    for product in dairy_products:
        db.session.add(product)

    # Commit the changes
    db.session.commit()


def print_tables():
    """
    Print all data from the tables to the console.
    """
    print("Users:")
    for user in User.query.all():
        print(user)
    print("\nCustomers:")
    for customer in Customer.query.all():
        print(customer)
    print("\nManagers:")
    for manager in Manager.query.all():
        print(manager)
    print("\nProducts:")
    for product in Product.query.all():
        print(product)
    print("\nCart Items:")
    for item in Cart.query.all():
        print(item)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # clear_tables()
        populate_data()
        print_tables()
