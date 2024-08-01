from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from app.routes import  carrito_routes, principal_routes, product_routes
    app.register_blueprint(carrito_routes.bp)
    app.register_blueprint(principal_routes.bp)
    app.register_blueprint(product_routes.bp)

    return app