from flask import Blueprint, render_template, request, redirect, url_for
from app.models.product import Product
from app.routes.carrito_routes import carrito_buy

bp = Blueprint('product', __name__)