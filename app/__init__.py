from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_pagedown import PageDown
from flask_moment import Moment

from config import DevConfig

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = '请登陆后查看'
moment = Moment()
page_down = PageDown()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    page_down.init_app(app)

    from app.home import home as home_blueprint
    from app.auth import auth as auth_blueprint
    from app.api import api as api_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app
