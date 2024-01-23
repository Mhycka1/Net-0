from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db 

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("welcome.html")

@views.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")

@views.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    if request.method == 'POST':
        electric_bill = float(request.form.get('electric-bill')) * 105
        gas_bill = float(request.form.get('gas-bill')) * 105
        oil_bill = float(request.form.get('oil-bill')) * 113
        car_mileage = float(request.form.get('car-mileage')) * 0.79
        sub_4_flights = float(request.form.get('flights-less-than-4-hours')) * 1100
        over_4_flights = float(request.form.get('flights-more-than-4-hours')) * 4400
        recycle_newspaper = request.form.get('recycle-newspaper')
        recycle_metal = request.form.get('recycle-aluminum-tin')

        footprint = electric_bill + gas_bill + oil_bill + car_mileage + sub_4_flights + over_4_flights

        if recycle_newspaper == 'n':
            footprint = footprint + 184
        
        if recycle_metal == 'n':
            footprint = footprint + 166
        
        user = User.query.filter_by(id=current_user.id).first()
        user.footprint_score = footprint
        db.session.commit()
        return redirect(url_for('views.main_dashboard')) 
    return render_template("quiz.html", user=current_user)

@views.route('/main_dashboard')
@login_required
def main_dashboard():
    return render_template("main_dashboard.html", user=current_user)

@views.route('/groups')
@login_required
def groups():
    return render_template("groups.html", user=current_user)

@views.route('/recap')
@login_required
def recap():
    return render_template("recap.html", user=current_user)