from flask import jsonify, request, url_for

from app.api import api
from app.auth.modles import User


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
