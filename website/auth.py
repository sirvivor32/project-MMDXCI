from xmlrpc.client import boolean
from flask import Blueprint, render_template,request,flash,redirect,url_for
from . import db
from .models import User,Note
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint ('auth',__name__)

@auth.route('/')
def home():
    return render_template('home.html')

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        Email= request.form.get("email")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        Password1 = request.form.get('password1')
        Password2 = request.form.get('password2')
            
        user = User.query.filter_by(email=Email).first()
    
        if user:
           flash('Email already exists!', category='error')
        elif len(Email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif len(firstname) < 2:
            flash('first name must be greater than 4 characters', category='error')      
        elif Password1 != Password2:
            flash('passwords must match!', category='error')           
        elif len(Password1) > 10:
            flash('password must be less than 10 characters', category='error')
            
        else:
            #add user
            new_user = User( email= Email, password = generate_password_hash(Password1, method="sha256"),)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
            return redirect(url_for('views.home'))



    return render_template('sign_up.html')

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password= request.form.get('password')
       
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succesfully!', category='success')
            else:
                flash('incorrect password! try again.', category='error')
        else:
            flash('Email doesnt exist', category='error')
   
    return render_template('login.html')