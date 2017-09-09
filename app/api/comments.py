from flask import jsonify, request, url_for

from app.api import api
from app.home.models import Comment


@api.route('/comments/<int:comment_id>/')
def get_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    return jsonify(comment.to_json())


@api.route('/articles/<int:article_id>/comments/')
def get_comments(article_id):
    page = request.args.get('page', 1, int)
    pagination = Comment.query.filter_by(
        article_id=article_id
    ).paginate(
        page,
        per_page=3
    )
    comments = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for(
            'api.get_comments',
            article_id=article_id,
            page=page - 1,
            _external=True
        )
    next = None
    if pagination.has_next:
        next = url_for(
            'api.get_comments',
            article_id=article_id,
            page=page + 1,
            _external=True
        )
    return jsonify({
        'commetens': [comment.to_json() for comment in comments],
        'perv': prev,
        'next': next
    })
