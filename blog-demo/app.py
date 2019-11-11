from os.path import join

from flask import Flask, render_template, request, url_for, redirect, session, Response

import cfg
from model import db, User, Article

app = Flask(__name__)
app.config.from_object(cfg)
db.init_app(app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    # db.drop_all()
    # db.create_all()
    article_list = Article.query.filter().order_by(Article.id).all()[:-6:-1]

    return render_template('blog.html', article=article_list)


@app.route('/article/<int:aid>/')
def article_list(aid):
    article = Article.query.filter(Article.id == aid).first()
    user = User.query.filter(User.id == article.user_id).first()
    return render_template('sidebar.html', article=article,user=user)



@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        user = User.query.filter(User.name == name).first()
        if user and name != '':
            if pwd == user.pwd and pwd != '':
                session['username'] = name
                session['password'] = pwd
                # r = Response()
                # r.set_cookie('session')
                return redirect(join('/home/', name))
            else:
                return render_template('login.html', error='密码错误')
        else:
            return render_template('login.html', error='该用户不存在')
    return render_template('login.html')


@app.route('/home/<string:username>/')
def home(username):
    username = request.cookies.get('username')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(Debug=True)
