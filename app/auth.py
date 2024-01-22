from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.main_dashboard'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Incorrect username', category='error')
    return render_template("login.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        firstname = request.form.get('first-name')
        lastname = request.form.get('last-name')
        age = int(request.form.get('age'))
        location = request.form.get('location')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username is taken', category='error')
        elif firstname == None or len(firstname) < 2:
            flash('First name must be greater than 2 characters', category='error')
        elif lastname == None or len(lastname) < 2:
            flash('Last name must be greater than 2 characters', category='error')
        elif age == None or age < 16:
            flash('Age must be at least 16', category='error')
        elif location == None or len(location) == 0:
            flash('please enter your location', category='error')
        elif email == None or len(email) < 3:
            flash('Email must be at least 3 characters')
        elif username == None or len(username) < 3:
            flash('Username must be at least 3 characters')
        elif password == None or len(password) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(firstname=firstname, lastname=lastname, age=age, location=location, email=email, username=username, password=generate_password_hash(password, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.quiz'))

    return render_template("sign-up.html")