from flask_httpauth import HTTPBasicAuth
from flask import g, make_response, jsonify

from app.auth.models import User
from app.api import api

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    if user.verify_password(password):
        g.current_user = user
        return True
    return False


@auth.error_handler
def auth_error():
    return make_response(jsonify({
        'error': '权限不允许'
    }), 401)


@api.before_request
@auth.login_required
def before_request():
    if not g.current_user:
        return make_response(jsonify({
            'error': '账户或密码错误'
        }), 403)
    elif not g.current_user.confirmed:
        return make_response(jsonify({
            'error': '帐号未激活'
        }), 403)
