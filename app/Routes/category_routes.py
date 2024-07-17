from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.Models.category import Category
from app import db

bp = Blueprint('category', __name__)

bp.route('/Category')
def index():
    data = Category.query.all()
    return render_template('', data=data)