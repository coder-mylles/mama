from flask import render_template
from flask_login import login_required
# from app import create_app
from . import main 

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/checkout')
def checkout():
    return render_template('checkout.html')

@main.route('/addcart')
@login_required
def cart():
    return render_template('cart.html')
