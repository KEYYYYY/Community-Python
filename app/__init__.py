from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import DevConfig

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    login_manager.init_app(app)

    from app.home import views as home_views
    from app.auth import views as auth_views
    app.register_blueprint(home_views.home)
    app.register_blueprint(auth_views.auth, url_prefix='/auth')
    return app
