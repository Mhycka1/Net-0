from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("welcome.html")

@views.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")

@views.route('/quiz', methods=['GET', 'POST'])
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
        print(footprint)

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