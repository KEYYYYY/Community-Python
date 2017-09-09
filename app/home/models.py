from datetime import datetime
import bleach

from markdown import markdown
from flask import url_for

from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text)
    content_html = db.Column(db.Text)
    page_view = db.Column(db.Integer, default=0)
    publish_time = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship(
        'Comment',
        backref='article',
        lazy='dynamic'
    )

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return '<Article {title}>'.format(
            title=self.title
        )

    def change_content(self):
        # 将markdown原文本转化为html代码
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote',
                        'code', 'em', 'i', 'li', 'ol', 'pre', 'strong',
                        'ul', 'h1', 'h2', 'h3', 'p'
                        ]
        self.content_html = bleach.linkify(bleach.clean(
            markdown(self.content, output_format='html'),
            tags=allowed_tags,
            strip=True
        ))

    def to_json(self):
        json_article = {
            'author': url_for(
                'api.get_user',
                user_id=self.author_id,
                _external=True
            ),
            'title': self.title,
            'content': self.content,
            'content_html': self.content_html,
            'comments_count': self.comments.count(),
            'comments': url_for(
                'api.get_comments',
                article_id=self.id,
                _external=True
            )
        }
        return json_article


class Follow(db.Model):
    follower_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        primary_key=True
    )
    followed_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        primary_key=True
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    content = db.Column(db.Text, nullable=False)
    content_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def change_content(self):
        # 将markdown原文本转化为html代码
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote',
                        'code', 'em', 'i', 'li', 'ol', 'pre', 'strong',
                        'ul', 'h1', 'h2', 'h3', 'p'
                        ]
        self.content_html = bleach.linkify(bleach.clean(
            markdown(self.content, output_format='html'),
            tags=allowed_tags,
            strip=True
        ))

    def to_json(self):
        json_comment = {
            'user': url_for(
                'api.get_user',
                user_id=self.user_id,
                _external=True
            ),
            'article': url_for(
                'api.get_article',
                article_id=self.article_id,
                _external=True
            ),
            'content': self.content,
            'content_html': self.content_html,
            'timestamp': self.timestamp
        }
        return json_comment
