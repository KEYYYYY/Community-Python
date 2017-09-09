from datetime import datetime
import hashlib

from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, url_for
from flask_login import UserMixin
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import db
from app.home.models import Follow


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    email = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(256), default='中国')
    about_me = db.Column(db.Text)
    password_hash = db.Column(db.String(128), nullable=False)
    avatar_hash = db.Column(db.String(64))
    confirmed = db.Column(db.Boolean, default=False)
    add_time = db.Column(db.DateTime, default=datetime.utcnow)
    articles = db.relationship('Article', backref='author', lazy='dynamic')
    followers = db.relationship(
        'Follow',
        foreign_keys=[Follow.followed_id],
        backref=db.backref('followed', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    )
    followed = db.relationship(
        'Follow',
        foreign_keys=[Follow.follower_id],
        backref=db.backref('follower', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    )
    comments = db.relationship(
        'Comment',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, email, password):
        self.email = email
        self.username = self.email
        self.password = password
        self.avatar_hash = hashlib.md5(self.email.encode('UTF-8')).hexdigest()

    def gravatar(self, size=100, default='identicon', rating='g'):
        """得到头像URL"""
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash_num = self.avatar_hash or hashlib.md5(
            self.email.encode('UTF-8')
        ).hexdigest()
        return '{url}/{hash_num}?s={size}&d={default}&r={rating}'.format(
            url=url,
            hash_num=hash_num,
            size=size,
            default=default,
            rating=rating
        )

    def generate_confirmation_token(self, expiration=3600):
        """产生激活帐号令牌"""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({
            'confirm': self.id
        })

    def confirm(self, token):
        """激活帐号"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True

    @property
    def password(self):
        raise AttributeError('不能访问密码！')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {0}>'.format(self.email)

    def is_following(self, user):
        return any(self.followed.filter_by(
            followed_id=user.id
        ))

    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)
            db.session.commit()

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)
            db.session.commit()

    def to_json(self):
        json_user = {
            'username': self.username,
            'email': self.email,
            'about_me': self.about_me,
            'confirmed': self.confirmed,
            'location': self.location,
            'add_time': self.add_time,
        }
        return json_user
