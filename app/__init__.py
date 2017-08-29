from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig
from app.home import views

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy()


def create_app():
    db.init_app(app)
    app.register_blueprint(views.home)
    return app
