from datetime import datetime

from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text)
    page_view = db.Column(db.Integer, default=0)
    publish_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return '<Article {title}>'.format(
            title=self.title
        )
