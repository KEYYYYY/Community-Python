import os

BASE_DIR = os.path.join(os.path.dirname(__file__))


class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = '763997136'
