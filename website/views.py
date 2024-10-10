from flask import Blueprint, render_template
from flask_login import login_required
from flask import request, redirect, url_for

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if 'login' in request.cookies:
        return render_template("home.html")
    return redirect(url_for('auth.login'))


@views.route('/ml', methods=['GET', 'POST'])
def machine_learning():
    return render_template("ml.html")


@views.route('/other-achievements', methods=['GET', 'POST'])
def other_achievements():
    return render_template("other_achievements.html")


@views.route('/software', methods = ['GET', 'POST'])
def software():
    return render_template("software.html")


@views.route('/computer-vision', methods=['GET', 'POST'])
def computer_vision():
    return render_template("computer_vision.html")
