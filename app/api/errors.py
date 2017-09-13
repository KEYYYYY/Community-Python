from flask import jsonify


def forbidden(message):
    response = jsonify({
        'error': '访问失败',
        'message': message
    })
    return response
