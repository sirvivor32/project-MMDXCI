from flask import Blueprint, render_template
auth = Blueprint ('auth',__name__)

@auth.route('/')
def home():
    return render_template('home.html')
@auth.route('/login')
def login():
    return '<p>Login</p>'

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up')
def sign_up():
    return '<p>sign up</p>'