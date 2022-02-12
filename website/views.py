from flask import Blueprint, render_template,Request,flash,redirect,url_for
from flask_login import login_required, login_user, logout_user
from . import db
from .models import User
views=Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html')
