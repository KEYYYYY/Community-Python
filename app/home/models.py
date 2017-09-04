from datetime import datetime
import bleach

from markdown import markdown

from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text)
    content_html = db.Column(db.Text)
    page_view = db.Column(db.Integer, default=0)
    publish_time = db.Column(db.DateTime, default=datetime.utcnow)

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
