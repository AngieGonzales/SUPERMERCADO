from app import db

class Customer(db.Model):
    __tablename__ = 'customer'
    idCustomer = db.Column(db.Integer, primary_key=True)
    nameCustomer = db.Column(db.String(25), nullable=False)
    addressCustomer = db.Column(db.String(25), nullable=False)
    phoneCustomer = db.Column(db.String(25), nullable=False)
    emailCustomer = db.Column(db.String(25), nullable=False)
    nameUser = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    sales = db.relationship("Sale", back_populates="customer")