from flask import Flask
from flask_login import LoginManager
import os
def create_app():
    app = Flask(__name__, )
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # login_manager.login_view = 'auth.login'
    # @login_manager.user_loader

    return app