from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("welcome.html")

@views.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")

@views.route('/quiz')
def quiz():
    return render_template("quiz.html")

@views.route('/main_dashboard')
def main_dashboard():
    return render_template("main_dashboard.html")

@views.route('/groups')
def groups():
    return render_template("groups.html")

@views.route('/recap')
def recap():
    return render_template("recap.html")