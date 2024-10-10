from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, login_required, current_user
from website.gg_sheet import GoogleSheetClient

from dotenv import load_dotenv
import os
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
            flash(f"Welcome {full_name} to join in my personal website", category='success')
            from datetime import datetime
            now = datetime.now()
            dtString = now.strftime('%d/%m/%Y-%H:%M:%S')
            load_dotenv()
            sheet = GoogleSheetClient(os.getenv('DATABASE'), 'database')
            sheet.write_in4_to_spreadsheet(email, full_name, dtString)
            resp = redirect(url_for('views.home'))
            resp.set_cookie('login', 'true')
            return resp
    return render_template("login.html")