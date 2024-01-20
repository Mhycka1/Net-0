from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    return render_template("login.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        firstname = request.form.get('first-name')
        lastname = request.form.get('lastname')
        age = request.form.get('age')
        location = request.form.get('location')
        email = request.form.get('email')
        password = request.form.get('password')

        if firstname == None or len(firstname) < 2:
            flash('First name must be greater than 2 characters', category='error')
        elif lastname == None or len(lastname) < 2:
            flash('Last name must be greater than 2 characters', category='error')
        elif age == None or age < 16:
            flash('Age must be at least 16', category='error')
        elif location == None or len(location) == 0:
            flash('please enter your location', category='error')
        elif email == None or len(email) < 3:
            flash('Email must be greater than 3 characters')
        elif password == None or len(password) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign-up.html")