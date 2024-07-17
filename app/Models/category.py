from app import db

class Category(db.Model):
    __tablename__ = 'category'
    idCategory = db.Column(db.Integer, primary_key=True)
    nameCategory = db.Column(db.String(25), nullable=False)
    desCategory = db.Column(db.String(225), nullable=False)
    
    