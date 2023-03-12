from flask import Blueprint, render_template, request, redirect, url_for, flash
from StackFusion.models import *
from StackFusion.main.utils import *
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return redirect(url_for('main.user_form'))

@main.route('/user-form', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        dob = request.form.get('dob')
        dob = datetime.strptime(dob, '%Y-%m-%d')
        # Send Email
        send_email(email)
        detail = Details(name=name, email=email, phone_number=phone_number, dob=dob)
        db.session.add(detail)
        db.session.commit()
        flash("Form submitted successfully.", "success")
        return redirect(url_for('main.submitted'))
    return render_template('index.html')

@main.route('/submitted', methods=['GET'])
def submitted():
    users = Details.query.all()
    return render_template('submitted.html', users=users)
