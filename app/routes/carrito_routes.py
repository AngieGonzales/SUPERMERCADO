from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.product import Product
from app.models.carrito import Carrito

bp = Blueprint('carritos', __name__)
carrito_buy = Carrito()

@bp.route('/carritoCompras')
def list():
    items = carrito_buy.getItems()
    return render_template('products/list.html', items=items)

@bp.route('/ListarProductos')
def principal():
    products = Product.query.all()
    return render_template('principales/principal.html', products=products)

@bp.route('/add/<int:id>', methods=['POST'])
def add_to_car(id):
    quantity = int(request.form[quantity])
    carrito_buy.add_product(id, quantity)
    return redirect(url_for('carritos.principal'))

@bp.route('/realizar_compra')
def realize_buy():
    total = carrito_buy.calculate_total()
    return render_template('realizar_compra.html', total=total)

@bp.route('/generar_factura', methods=['POST'])
def generate_bill():
    total = carrito_buy.calculate_total()
    carrito_buy.clearcarrito = ()
    return render_template('factura.html', total = total)

@bp.route('/itemscarrito', methods=['GET', 'POST'])
def tcarrito():
    a = carrito_buy.sizeD()
    print("Entra a carrito rutas", a)
    return f"Entra a carrito {carrito_buy.sizeD()}"