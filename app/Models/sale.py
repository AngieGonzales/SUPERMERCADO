from app import db

class Sale(db.Model):
    __tablename__ = 'sale'
    idSale = db.Column(db.Integer, primar_key=True)
    nameProductS = db.Column(db.String(25), nullable=False)
    totalPriceS = db.Column(db.String(25), nullable=False)
    quantitySale = db.Column(db.String(25), nullable=False)
    dateSale = db.Column(db.String(25), nullable=False)

    id_customer = db.Column(db.Integer, db.ForeignKey('customer.idCustomer'))
    id_employee = db.Column(db.Integer, db.ForeignKey('employee.idEmployee'))