from flask import Blueprint, render_template,Request,flash,redirect,url_for
views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')
