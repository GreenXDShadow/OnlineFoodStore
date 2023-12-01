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
    customer1 = Customer(name="JaneDoe", password="password456", email="janedoe@example.com")
    manager1 = Manager(name="AdminUser", password="adminpass", email="admin@example.com")
    customer2 = Customer(name="a", password="a",email="a@a.com")

    db.session.add(customer1)
    db.session.add(manager1)

    # Default dairy products with prices added
    dairy_products = [
        Product(name="Milk", weight=1.0, type="packaged", category="dairy", price=2.99, imagePath="Icons/milk.png", quantity=10, amount=None),
        Product(name="that Cheese", weight=0.5, type="packaged", category="dairy", price=4.50, imagePath="Icons/cheese.png", quantity=10, amount=None),
        Product(name="Eggsssss", weight=0.6, type="packaged", category="dairy", price=3.20, imagePath="Icons/eggs.png", quantity=10, amount=None),
        Product(name="Almond Milk", weight=1.0, type="packaged", category="dairy", price=3.99, imagePath="Icons/almondmilk.png", quantity=10, amount=None),
        Product(name="Yogurt", weight=0.4, type="packaged", category="dairy", price=1.50, imagePath="Icons/yogurt.png", quantity=10, amount=None),
        Product(name="Butter", weight=0.25, type="packaged", category="dairy", price=2.25, imagePath="Icons/butter.png", quantity=10, amount=None),
        Product(name="Whipped Cream", weight=0.2, type="packaged", category="dairy", price=2.00,imagePath="Icons/whippedcream.png", quantity=10, amount=None),
        Product(name="Soy Milk", weight=1.0, type="packaged", category="dairy", price=3.99,imagePath="Icons/soymilk.png", quantity=10, amount=None)
    ]

    frozen_food_products = [
        Product(name="Pizza", weight=0.8, type="packaged", category="frozen", price=6.99, imagePath="Icons/pizza.png", quantity=10, amount=None),
        Product(name="Berries", weight=0.5, type="packaged", category="frozen", price=4.50, imagePath="Icons/berries.png", quantity=10, amount=None),
        Product(name="Peas", weight=0.6, type="packaged", category="frozen", price=2.99, imagePath="Icons/peas.png", quantity=10, amount=None),
        Product(name="Fish Sticks", weight=0.7, type="packaged", category="frozen", price=5.50, imagePath="Icons/fishsticks.png", quantity=10, amount=None),
        Product(name="Spinach", weight=0.4, type="packaged", category="frozen", price=3.25, imagePath="Icons/spinach.png", quantity=10, amount=None),
        Product(name="Mushrooms", weight=0.3, type="packaged", category="frozen", price=3.75, imagePath="Icons/mushrooms.png", quantity=10, amount=None),
        Product(name="Chicken Nuggets", weight=0.6, type="packaged", category="frozen", price=4.99, imagePath="Icons/nuggets.png", quantity=1, amount=None),
        Product(name="Shrimp", weight=0.5, type="packaged", category="frozen", price=7.99, imagePath="Icons/shrimp.png", quantity=10, amount=None)
    ]

    # Beverage products
    beverage_products = [
        Product(name="Orange Juice", weight=1.0, type="packaged", category="beverages", price=3.99, imagePath="Icons/orangejuice.png", quantity=10, amount=None),
        Product(name="Water", weight=1.0, type="packaged", category="beverages", price=1.00, imagePath="Icons/water.png", quantity=10, amount=None),
        Product(name="Grape Juice", weight=1.0, type="packaged", category="beverages", price=4.20, imagePath="Icons/grapejuice.png", quantity=10, amount=None),
        Product(name="Apple Cider", weight=1.0, type="packaged", category="beverages", price=5.00, imagePath="Icons/applecider.png", quantity=10, amount=None),
        Product(name="Berry Smoothie", weight=0.5, type="packaged", category="beverages", price=3.50, imagePath="Icons/berrysmoothie.png", quantity=10, amount=None),
        Product(name="Lemonade", weight=1.0, type="packaged", category="beverages", price=2.75, imagePath="Icons/lemonade.png", quantity=10, amount=None),
        Product(name="Green Tea", weight=0.5, type="packaged", category="beverages", price=2.50, imagePath="Icons/greentea.png", quantity=10, amount=None),
        Product(name="Watermelon Juice", weight=1.0, type="packaged", category="beverages", price=4.00, imagePath="Icons/watermelonjuice.png", quantity=10, amount=None)
    ]

    # Fruit products
    # TODO: Change the quantity to amount since loose items can be bought by weight
    fruit_products = [
        Product(name="Apple", weight=0.2, type="fresh", category="fruit", price=0.30, imagePath="Icons/apple.png", quantity=0, amount=10),
        Product(name="Apricot", weight=0.1, type="fresh", category="fruit", price=0.40, imagePath="Icons/apricot.png", quantity=0, amount=10),
        Product(name="Grape", weight=0.5, type="fresh", category="fruit", price=2.50, imagePath="Icons/grape.png", quantity=0, amount=10),
        Product(name="Banana", weight=0.2, type="fresh", category="fruit", price=0.20, imagePath="Icons/banana.png", quantity=0, amount=10),
        Product(name="Blueberry", weight=0.2, type="fresh", category="fruit", price=3.00, imagePath="Icons/blueberry.png", quantity=0, amount=10),
        Product(name="Blackberry", weight=0.2, type="fresh", category="fruit", price=3.00, imagePath="Icons/blackberry.png", quantity=0, amount=10),
        Product(name="Orange", weight=0.3, type="fresh", category="fruit", price=0.50, imagePath="Icons/orange.png", quantity=0, amount=10),
        Product(name="Cherry", weight=0.2, type="fresh", category="fruit", price=0.60, imagePath="Icons/cherry.png", quantity=0, amount=10)
    ]

    vegetable_products = [
        Product(name="Tomato", weight=0.3, type="fresh", category="vegetable", price=1.00, imagePath="Icons/tomato.png", quantity=0, amount=10),
        Product(name="Green Onion", weight=0.05, type="fresh", category="vegetable", price=0.20, imagePath="Icons/greenonion.png", quantity=0, amount=10),
        Product(name="Cucumber", weight=0.4, type="fresh", category="vegetable", price=0.75, imagePath="Icons/cucumber.png", quantity=0, amount=10),
        Product(name="Carrot", weight=0.1, type="fresh", category="vegetable", price=0.30, imagePath="Icons/carrots.png", quantity=0, amount=10),
        Product(name="Broccoli", weight=0.5, type="fresh", category="vegetable", price=1.50, imagePath="Icons/broccoli.png", quantity=0, amount=10),
        Product(name="Cauliflower", weight=0.6, type="fresh", category="vegetable", price=1.80, imagePath="Icons/cauliflower.png", quantity=0, amount=10),
        Product(name="Cabbage", weight=0.7, type="fresh", category="vegetable", price=1.20, imagePath="Icons/cabbage.png", quantity=0, amount=10),
        Product(name="Potato", weight=0.4, type="fresh", category="vegetable", price=0.50, imagePath="Icons/potato.png", quantity=0, amount=10)
    ]

    # TODO: Meat should also be in amount since it is a loose product
    # Meat Products with Prices
    meat_products = [
        Product(name="Ham", weight=1.0, type="packaged", category="meat", price=5.99, imagePath="Icons/ham.png", quantity=1, amount=None),
        Product(name="Lamb Shank", weight=1.2, type="fresh", category="meat", price=14.99, imagePath="Icons/lambshank.png", quantity=0, amount=10),
        Product(name="Sausage", weight=0.6, type="packaged", category="meat", price=4.50, imagePath="Icons/sausages.png", quantity=1, amount=None),
        Product(name="Ground Beef", weight=1.0, type="fresh", category="meat", price=7.99, imagePath="Icons/groundbeef.png", quantity=0, amount=10),
        Product(name="Chicken", weight=1.5, type="fresh", category="meat", price=6.50, imagePath="Icons/chicken.png", quantity=0, amount=10),
        Product(name="Beef Steak", weight=1.0, type="fresh", category="meat", price=12.99, imagePath="Icons/beef.png", quantity=0, amount=10),
        Product(name="Pork Chop", weight=0.8, type="fresh", category="meat", price=8.99, imagePath="Icons/chop.png", quantity=0, amount=10),
        Product(name="Bacon", weight=0.5, type="packaged", category="meat", price=4.99, imagePath="Icons/bacon.png", quantity=0, amount=None)
    ]

    # Loop for adding dairy products to the database
    for product in dairy_products:
        db.session.add(product)

    for product in vegetable_products:
        db.session.add(product)


    # Loop for adding frozen food products to the database
    for product in frozen_food_products:
        db.session.add(product)

    # Loop for adding beverage products to the database
    for product in beverage_products:
        db.session.add(product)

    # Loop for adding fruit products to the database
    for product in fruit_products:
        db.session.add(product)

    # Loop for adding meat products to the database
    for product in meat_products:
        db.session.add(product)

    # Commit the changes to the database
    db.session.commit()

    # Commit the changes
    db.session.commit()

def search_products(query):
    # Perform a database query to find products that match the search query
    results = Product.query.filter(
        (Product.name.ilike(f"%{query}%")) |
        (Product.category.ilike(f"%{query}%"))
    ).all()

    return results


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
        clear_tables()
        populate_data()
        print_tables()
