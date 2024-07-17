from app import db

class Product(db.Model):
    __talename__ = 'product'
    idProduct = db.Column(db.Integer, primary_key=True)
    nameProduct = db.Column(db.String(225), nullable=False)
    desProduct = db.Column(db.String(225), nullable=False)
    priceProduct = db.Column(db.Float, nullable=False)
    nameProduct = db.Column(db.String(225), nullable=False)
    stock = db.Column(db.Float(225), nullable=False)

    id_category = db.Column(db.Integer, db.ForeignKey('category.idCategory'))