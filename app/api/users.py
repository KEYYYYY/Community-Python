from flask import jsonify, request, url_for, make_response

from app.api import api
from app.auth.models import User
from app import db
from app.auth.views import send_email


@api.route('/users/<int:user_id>/')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_json())


@api.route('/users/')
def get_users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(
        page,
        per_page=3
    )
    users = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_users', page=page - 1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_users', page=page + 1, _external=True)
    return jsonify({
        'users': [user.to_json() for user in users],
        'prev': prev,
        'next': next
    })


@api.route('/users/', methods=['POST'])
def register():
    try:
        data = request.get_json(force=True)
        email = data['email']
        password = data['password']
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(
            to=user.email,
            subject='请激活您的帐号',
            template='confirm.html',
            token=token
        )
        return make_response(jsonify({
            'ok': '注册成功，请尽快激活您的帐号'
        }), 201)
    except:
        return make_response(jsonify({
            'error': '注册失败'
        }), 400)
