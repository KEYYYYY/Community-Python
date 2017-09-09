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

    from app.home import views as home_view
    from app.auth import views as auth_views
    from app.api import api
    app.register_blueprint(home_view.home)
    app.register_blueprint(auth_views.auth, url_prefix='/auth')
    app.register_blueprint(api, url_prefix='/api')
    return app
