
from app import app, db
from User import User, Customer, Manager, Cart
from Product import Product, BoxedProduct, FreshProduct

def populate_data():
    # Clear existing data
    # Cart.query.delete()
    # BoxedProduct.query.delete()
    # FreshProduct.query.delete()
    # Customer.query.delete()
    # Manager.query.delete()
    # User.query.delete()
    # Product.query.delete()

    # # Populate User, Customer, and Manager
    # user1 = User(name="JohnDoe", password="password123", email="johndoe@example.com")
    # customer1 = Customer(name="JaneDoe", password="password456", email="janedoe@example.com", address="123 Main St", card_number_last4="1234", expiration_month="12", expiration_year="2025")
    # manager1 = Manager(name="AdminUser", password="adminpass", email="admin@example.com")
    #
    # db.session.add(user1)
    # db.session.add(customer1)
    # db.session.add(manager1)
    #
    # # Populate Product, BoxedProduct, and FreshProduct
    # product1 = Product(name="GenericProduct", weight=1.5)
    # boxed_product1 = BoxedProduct(name="BoxedCereal", weight=1.0, cost=5.99)
    # fresh_product1 = FreshProduct(name="FreshApple", costPerPound=1.99)
    #
    # db.session.add(product1)
    # db.session.add(boxed_product1)
    # db.session.add(fresh_product1)
    #
    # # Commit the changes
    # db.session.commit()
    #
    # # Add some products to the customer's cart
    # cart_item1 = Cart(customer_id=customer1.id, product_id=boxed_product1.id)
    # cart_item2 = Cart(customer_id=customer1.id, product_id=fresh_product1.id)
    #
    # db.session.add(cart_item1)
    # db.session.add(cart_item2)
    # db.session.commit()

    # Print the data to console
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
    print("\nBoxedProducts:")
    for product in BoxedProduct.query.all():
        print(product)
    print("\nFreshProducts:")
    for product in FreshProduct.query.all():
        print(product)
    print("\nCart Items:")
    for item in Cart.query.all():
        print(item)

if __name__ == '__main__':
    with app.app_context():
        populate_data()
