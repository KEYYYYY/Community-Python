from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.now)

    @property
    def password(self):
        raise AttributeError('不能访问密码！')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {0}>'.format(self.username)
