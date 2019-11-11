from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user

from app.forms import UpdateForm, AddForm
from app.model import Post, db, User

admin = Blueprint('admin', __name__, url_prefix='/admin')


@login_required
@admin.route("/")
def admin_index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.filter().order_by(Post.time.desc()).paginate(page=page, per_page=5)
    posts = pagination.items
    user = current_user.uname
    return render_template('admin/index.html', posts=posts, user=user)


@login_required
@admin.route('/update/<int:i>', methods=['GET', 'POST'])
def update(i):
    user = current_user.uname
    post = Post.query.filter(Post.pid == i).first()
    form = UpdateForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            head = form.head.data
            body = form.body.data
            print(i)
            p = Post.query.get(i)
            p.title = title
            p.head = head
            p.body = body
            db.session.commit()  # 提交
            return redirect('/admin/')
        return '修改失败，请重试'

    return render_template('admin/update.html', post=post, form=form,user=user)


@login_required
@admin.route('/delete/<int:j>')
def delete(j):

    p = Post.query.get(j)  # 需要删除的对象
    db.session.delete(p)  # 删除
    db.session.commit()  # 提交事务
    return redirect('/admin/')

@login_required
@admin.route('/user/', methods=['GET', 'POST'])
def user():
    user = current_user.uname
    u=User.query.filter(User.uname==user).first()

    return render_template('admin/user.html',user=user,u=u)


@login_required
@admin.route('/add/', methods=['GET', 'POST'])
def add():
    user = current_user.uname
    form = AddForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            author= current_user.uname
            head = form.head.data
            body = form.body.data
            user = User.query.filter(User.uname==author).first()
            author_id = user.uid
            post = Post(title=title,author_id=author_id, head=head, body=body,user=user)
            db.session.add(post)
            db.session.commit()
            return redirect('/admin/')
        return '提交失败'

    return render_template('admin/add.html', form=form,user=user)
