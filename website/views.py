from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html")

@views.route('/ml', methods=['GET', 'POST'])
@login_required
def machine_learning():
    return render_template("ml.html")

@views.route('/other-achievements', methods=['GET', 'POST'])
@login_required
def other_achievements():
    return render_template("other_achievements.html")

@ views.route('/computer-vision', methods=['GET', 'POST'])
@login_required
def contact():
    return render_template("computer_vision.html")