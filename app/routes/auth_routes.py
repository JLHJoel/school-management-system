# app/routes/auth_routes.py
from flask import Blueprint, render_template

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login')
def login():
    return render_template('login.html')

@auth_routes.route('/register')
def register():
    return render_template('register.html')
