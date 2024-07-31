from flask import Blueprint, render_template, request, redirect, url_for
from app.models.category import Category
from app import db

bp = Blueprint('category', __name__)

@bp.route('/category')
def index():
    data = Category.query.all()
    return render_template('categorys/index.html', data=data)

@bp.route('/category/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nameCategory = request.form['nameCategory']
        desCategory = request.form['desCategory']
        
        new_category = Category(nameCategory=nameCategory, desCategory=desCategory)
        db.session.add(new_category)
        db.session.commit()
        
        return redirect(url_for('category.index'))

    return render_template('categorys/add.html')