from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, login_required, current_user
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('name')

        if len(email) < 10 or not "@gmail.com" in email:
            flash("Invalid email, please try again", category='danger')
        elif len(full_name) < 6:
            flash("Name must be greater than 5 character", category='danger')
        else:
            # flash(f"Welcome {full_name} to join in my personal website", category='success')
            return redirect(url_for('views.home'))
    return render_template("login.html")