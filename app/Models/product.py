from app import db

class Product(db.Model):
    __talename__ = 'product'
    idProduct = db.Column(db.Integer, primary_key=True)
    nameProduct = db.Column(db.String(225), nullable=False)
    priceProduct = db.Column(db.Float, nullable=False)
    weightProduct = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    id_category = db.Column(db.Integer, db.ForeignKey('category.idCategory'))

    sales = db.relationship("SaleDetail", back_populates="products")