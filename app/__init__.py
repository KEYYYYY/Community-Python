from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

from config import DevConfig

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = '请登陆后查看'


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.home import views as home_view
    from app.auth import views as auth_views
    app.register_blueprint(home_view.home)
    app.register_blueprint(auth_views.auth, url_prefix='/auth')
    return app
