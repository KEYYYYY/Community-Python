from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig
from app.home import views

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)

    app.register_blueprint(views.home)
    return app
