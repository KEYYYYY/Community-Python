from flask import jsonify, request, url_for

from app.api import api
from app.home.models import Article
from app import db


@api.route('/articles/<int:article_id>/')
def get_article(article_id):
    article = Article.query.get_or_404(article_id)
    return jsonify(article.to_json())


@api.route('/articles/', methods=['GET', 'POST'])
def get_articles():
    if request.method == 'GET':
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
    if request.method == 'POST':
        try:
            article = Article(
                title=request.args['title']
            )
            db.session.add(article)
            db.session.commit()
        except:
            return jsonify({
                'message': '必填字段为空'
            }), 400
        return 201
