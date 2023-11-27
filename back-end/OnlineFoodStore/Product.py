from app import db
class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    imagePath = db.Column(db.String)
    name = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float)
    type = db.Column(db.String(50))
    category = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    amount = db.Column(db.Float)

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, weight={self.weight}, type={self.type}, category={self.category})>"