from flask import jsonify, request, url_for

from app.api import api
from app.home.models import Article


@api.route('/articles/<int:article_id>/')
def get_article(article_id):
    article = Article.query.get_or_404(article_id)
    return jsonify(article.to_json())


@api.route('/articles/')
def get_articles():
    page = request.args.get('page', 1, int)
    pagination = Article.query.paginate(
        page,
        per_page=3
    )
    articles = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_articles', page=page - 1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_articles', page=page + 1, _external=True)
    return jsonify({
        'articles': [article.to_json() for article in articles],
        'prev': prev,
        'next': next
    })
