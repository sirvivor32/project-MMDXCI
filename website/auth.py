from flask import Blueprint, render_template,request,flash,redirect,url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint ('auth',__name__)

@auth.route('/')
def home():
    return render_template('home.html')
@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email=request.form.get('email')
        firstname = request.form.get('firstname')
        lastname= request.form.get('lastname')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        if len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
            pass
        elif len(firstname) < 2:
            flash('first name must be greater than 4 characters', category='error')
            pass
        elif password1 != password2:
            flash('passwords must match!', category='error')
            pass
        elif len(password1) > 10:
            flash('password must be less than 10 characters', category='error')
            pass
        else:
            #add user
            new_user = User( email= email, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
            return redirect(url_for('views.home'))



    return render_template('sign_up.html')