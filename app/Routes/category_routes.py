from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.category import Category
from app import db

bp = Blueprint('category', __name__)

bp.route('/Category')
def index():
    data = Category.query.all()
    return render_template('categorys/index.html', data=data)