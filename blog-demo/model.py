from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    pwd = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<User(name:%s)>' % self.name


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.relationship('User', backref='Article')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(1024), nullable=False)
    abstract = db.Column(db.String(128), nullable=False)  # 摘要
    content = db.Column(db.Text, nullable=False)  # 正文
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)
    visiting = db.Column(db.Integer, nullable=False)  # 访问量

    def __repr__(self):
        return '<User(name:%s)>' % self.title


class Comment(db.Model):
    __tablename__ = 'comment'  # 评论
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article = db.relationship('Article', backref=db.backref('comment', order_by=create_time.desc()))
