import os

BASE_DIR = os.path.join(os.path.dirname(__file__))


class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = '763997136'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USERNAME = '763997136@qq.com'
    MAIL_PASSWORD = '秘密'
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = '763997136@qq.com'
