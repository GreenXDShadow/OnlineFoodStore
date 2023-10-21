from app import db

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float)

    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'product',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, weight={self.weight})>"

class BoxedProduct(Product):
    __tablename__ = 'boxedproduct'

    id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    cost = db.Column(db.Float)

    __mapper_args__ = {
        'polymorphic_identity': 'boxedproduct',
    }

    def __repr__(self):
        return f"<BoxedProduct(id={self.id}, name={self.name}, weight={self.weight}, cost={self.cost})>"

class FreshProduct(Product):
    __tablename__ = 'freshproduct'

    id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    costPerPound = db.Column(db.Float)

    __mapper_args__ = {
        'polymorphic_identity': 'freshproduct',
    }

    def __repr__(self):
        return f"<FreshProduct(id={self.id}, name={self.name}, costPerPound={self.costPerPound})>"
