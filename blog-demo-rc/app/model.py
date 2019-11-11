from datetime import datetime

from flask_login._compat import unicode
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(30), unique=True)
    upass = db.Column(db.String(128))
    post = db.relationship('Post')  # 正向写法
    # name =db.Column(db.String(30))
    # email=db.Column(db.String(30), unique=True)
    # tel=db.Column(db.String(30), unique=True)
    # qq=db.Column(db.String(30), unique=True)
    # weibo=db.Column(db.String(30))
    # info=db.Column(db.Text)

    def get_id(self):
        return unicode(self.uid)


# post_category = db.Table(
#     'post_category',
#     db.Column('post_pid', db.Integer, db.ForeignKey('post.pid'),primary_key=True),
#     db.Column('category_cid', db.Integer, db.ForeignKey('category.cid'),primary_key=True)
# )
# post_tag = db.Table(
#     'post_tag',
#     db.Column('post_pid', db.Integer, db.ForeignKey('post.pid'),primary_key=True),
#     db.Column('tag_tid', db.Integer, db.ForeignKey('tag.tid'),primary_key=True)
# )
# class post_category(db.Model):
#     __tablename__ = 'post_category'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     post_pid = db.Column(db.Integer, db.ForeignKey('post.pid'))
#     tag_tid = db.Column(db.Integer, db.ForeignKey('tag.tid'))
#
#
# class post_tag(db.Model):
#     __tablename__ = 'post_tag'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     post_pid = db.Column(db.Integer, db.ForeignKey('post.pid'))
#     category_cid = db.Column(db.Integer, db.ForeignKey('category.cid'))


class Category(db.Model):
    __tablename__ = 'category'
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cname = db.Column(db.String(30), unique=True)
    # post = db.relationship('Post', back_populates='category', secondary='post_category')
    post = db.relationship('Post')

class Tag(db.Model):
    __tablename__ = 'tag'
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tname = db.Column(db.String(30), unique=True)
    # post = db.relationship('Post', back_populates='tag', secondary='post_tag')
    post = db.relationship('Post')

class Post(db.Model):
    __tablename__ = 'post'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.uid'))  #
    author = db.relationship('User', back_populates='post')  # user 一对多个 post
    time = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    title = db.Column(db.String(30), unique=True)
    head = db.Column(db.String(120))
    body = db.Column(db.Text)
    read = db.Column(db.Integer)
    category = db.relationship('Category', back_populates='post')
    category_id = db.Column(db.Integer, db.ForeignKey('category.cid'))
    tag = db.relationship('Tag', back_populates='post')
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.tid'))
    # category = db.relationship('Category', back_populates='post', secondary='post_category')
    # tag = db.relationship('Tag', back_populates='post', secondary='post_tag')


class Link(db.Model):
    lid = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(30))
    url = db.Column(db.String(255))
