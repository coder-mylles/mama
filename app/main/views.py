from flask import render_template
# from app import create_app
from . import main 

@main.route('/')
def index():
    return render_template('index.html')