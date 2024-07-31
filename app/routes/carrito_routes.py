from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.product import Product
from app.models.carrito import Carrito

bp = Blueprint('carritos', __name__)
carrito_buy = Carrito()

@bp.route('/')
def list():
    items = carrito_buy.getItems()
    return render_template('products/list.html', items=items)

@bp.route('/ListarProductos')
def index():
    products = carrito_buy
    return render_template('index.html', products=products)

@bp.route('/add/<int:idProduct', methods=['POST'])
def add_to_car(idProduct):
    quantity = int(request.form[idProduct, quantity])
    carrito_buy.add_product(idProduct, quantity)
    return redirect(url_for('product.index'))

@bp.route('/realizar_compra')
def realize_buy():
    total = carrito_buy.calculate_total()
    return render_template('realizar_compra.html', total=total)

@bp.route('/generar_factura', methods=['POST'])
def generate_bill():
    total = carrito_buy.calculate_total()
    carrito_buy.carrito = []
    return render_template('factura.html', total = total)

@bp.route('/itemscarrito', methods=['GET', 'POST'])
def tcarrito():
    a = carrito_buy.tamañoD()
    print("Entra a carrito rutas", a)
    return f"Entra a carrito {carrito_buy.tamañoD()}"