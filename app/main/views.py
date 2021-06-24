from flask import render_template
# from app import create_app
from . import main 

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/checkout')
def checkout():
    return render_template('checkout.html')

@main.route('/addcart')
def cart():
    return render_template('cart.html')
