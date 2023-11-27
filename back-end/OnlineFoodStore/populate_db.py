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

    # Frozen food products
    frozen_food_products = [
        Product(name="Pizza", weight=0.8, type="packaged", category="frozen", imagePath="Icons/pizza.png", quantity=1, amount=None),
        Product(name="Berries", weight=0.5, type="packaged", category="frozen", imagePath="Icons/berries.png", quantity=1, amount=None),
        Product(name="Peas", weight=0.6, type="packaged", category="frozen", imagePath="Icons/peas.png", quantity=1, amount=None),
        Product(name="Fish Sticks", weight=0.7, type="packaged", category="frozen", imagePath="Icons/fishsticks.png", quantity=1, amount=None),
        Product(name="Spinach", weight=0.4, type="packaged", category="frozen", imagePath="Icons/spinach.png", quantity=1, amount=None),
        Product(name="Mushrooms", weight=0.3, type="packaged", category="frozen", imagePath="Icons/mushrooms.png", quantity=1, amount=None),
        Product(name="Chicken Nuggets", weight=0.6, type="packaged", category="frozen", imagePath="Icons/nuggets.png", quantity=1, amount=None),
        Product(name="Shrimp", weight=0.5, type="packaged", category="frozen", imagePath="Icons/shrimp.png", quantity=1, amount=None)
    ]

    # Beverage products
    beverage_products = [
        Product(name="Orange Juice", weight=1.0, type="liquid", category="beverages", imagePath="Icons/orangejuice.png", quantity=1, amount=None),
        Product(name="Water", weight=1.0, type="liquid", category="beverages", imagePath="Icons/water.png", quantity=1, amount=None),
        Product(name="Grape Juice", weight=1.0, type="liquid", category="beverages", imagePath="Icons/grapejuice.png", quantity=1, amount=None),
        Product(name="Apple Cider", weight=1.0, type="liquid", category="beverages", imagePath="Icons/applecider.png", quantity=1, amount=None),
        Product(name="Berry Smoothie", weight=0.5, type="liquid", category="beverages", imagePath="Icons/berrysmoothie.png", quantity=1, amount=None),
        Product(name="Lemonade", weight=1.0, type="liquid", category="beverages", imagePath="Icons/lemonade.png", quantity=1, amount=None),
        Product(name="Green Tea", weight=0.5, type="liquid", category="beverages", imagePath="Icons/greentea.png", quantity=1, amount=None),
        Product(name="Watermelon Juice", weight=1.0, type="liquid", category="beverages", imagePath="Icons/watermelonjuice.png", quantity=1, amount=None)
    ]

    # Fruit products
    # TODO: Change the quantity to amount since loose items can be bought by weight
    fruit_products = [
        Product(name="Apple", weight=0.2, type="fresh", category="fruit", imagePath="Icons/apple.png", quantity=1, amount=None),
        Product(name="Apricot", weight=0.1, type="fresh", category="fruit", imagePath="Icons/apricot.png", quantity=1, amount=None),
        Product(name="Grape", weight=0.5, type="fresh", category="fruit", imagePath="Icons/grape.png", quantity=1, amount=None),
        Product(name="Banana", weight=0.2, type="fresh", category="fruit", imagePath="Icons/banana.png", quantity=1, amount=None),
        Product(name="Blueberry", weight=0.2, type="fresh", category="fruit", imagePath="Icons/blueberry.png", quantity=1, amount=None),
        Product(name="Blackberry", weight=0.2, type="fresh", category="fruit", imagePath="Icons/blackberry.png", quantity=1, amount=None),
        Product(name="Orange", weight=0.3, type="fresh", category="fruit", imagePath="Icons/orange.png", quantity=1, amount=None),
        Product(name="Cherry", weight=0.2, type="fresh", category="fruit", imagePath="Icons/cherry.png", quantity=1, amount=None)
    ]

    # TODO: Meat should also be in amount since it is a loose product
    # Meat products
    meat_products = [
        Product(name="Ham", weight=1.0, type="packaged", category="meat", imagePath="Icons/ham.png", quantity=1, amount=None),
        Product(name="Lamb Shank", weight=1.2, type="fresh", category="meat", imagePath="Icons/lambshank.png", quantity=1, amount=None),
        Product(name="Sausage", weight=0.6, type="packaged", category="meat", imagePath="Icons/sausages.png", quantity=1, amount=None),
        Product(name="Ground Beef", weight=1.0, type="fresh", category="meat", imagePath="Icons/groundbeef.png", quantity=1, amount=None),
        Product(name="Chicken", weight=1.5, type="fresh", category="meat", imagePath="Icons/chicken.png", quantity=1, amount=None),
        Product(name="Beef Steak", weight=1.0, type="fresh", category="meat", imagePath="Icons/beef.png", quantity=1, amount=None),
        Product(name="Pork Chop", weight=0.8, type="fresh", category="meat", imagePath="Icons/chop.png", quantity=1, amount=None),
        Product(name="Bacon", weight=0.5, type="packaged", category="meat", imagePath="Icons/bacon.png", quantity=1, amount=None)
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
