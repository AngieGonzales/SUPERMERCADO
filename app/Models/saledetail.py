from app import db

class SaleDetail(db.Model):
    __tablename__ = 'saledetail'
    idSaleDetail = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.String, nullable=False)
    unitPrice = db.Column(db.Float, nullable=False)
    subTotal = db.Column(db.Float, nullable=False)
    id_ale = db.Column(db.Integer, db.ForeignKey('sale.idSale'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.idProduct'))

    sale = db.relationship("Sale", back_populates="products")
    products = db.relationship("Product", back_populates="sales")