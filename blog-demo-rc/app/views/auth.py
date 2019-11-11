from flask import Blueprint, render_template, redirect, url_for, request, session
from flask_login import current_user, login_user, login_required, logout_user
import random
from app.forms import LoginForm,RegisterForm
from app.model import User, db

auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/admin/')
    form = LoginForm(request.form)
    code = random.randint(1000,9999)
    code = str(code)
    session['code'] = code
    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            code = form.code
            remember = form.remember.data
            user = User.query.filter().first()
            if user:
                if username == user.uname and password == user.upass:
                    login_user(user,remember)
                    print(login_user(user,remember))
                    return redirect('/admin/')
                else:
                    return 'Invalid username or password.', 'warning'
            return '表单提交成功'
        else:
            return '表单提交失败'

    return render_template('auth/login.html',form=form,code=code)


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect('/')


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    form = RegisterForm(request.form)
    code = random.randint(1000, 9999)
    code = str(code)
    session['code'] = code
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password2 = form.password2.data
            code = form.code
            user = User.query.filter(User.uname==username).first()
            if username != user.uname and username is not None:
                u = User(uname=username,upass=password)
                db.session.add(u)
                db.session.commit()
                return redirect('/admin/')
            else:
                return '用户已经存在'
        else:
            return '表单提交失败'
    return render_template('auth/register.html',form=form,code=code)
