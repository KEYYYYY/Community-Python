from flask_httpauth import HTTPBasicAuth
from flask_login import AnonymousUserMixin
from flask import g

from app.auth.modles import User
from app.api import api
from app.api.errors import forbidden

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    if email == '':
        g.current_user = AnonymousUserMixin()
        return True
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)


@api.before_request
@auth.login_required
def before_request():
    if not g.current_user.is_anonymous and \
            not g.current_user.confirmed:
        return forbidden('未通过验证')
