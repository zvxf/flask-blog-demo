from flask import Blueprint, render_template, request, current_app, url_for, redirect

from app.model import db, Post, Tag, Category

blog = Blueprint('blog', __name__, url_prefix='/')


@blog.route('/')
def index():
    # db.create_all()
    # posts = Post.query.filter().all()[:10]
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.filter().order_by(Post.time.desc()).paginate(page=page, per_page=5)
    posts = pagination.items
    title = '博客首页~'
    c = Category.query.filter().order_by(Category.cname).all()[:7]
    t = Tag.query.filter().order_by(Tag.tname).all()[:7]

    return render_template('blog/blog.html', posts=posts, pagination=pagination, title=title, c=c, t=t)


@blog.route('/category/<string:cname>/')
def category(cname):
    try:
        page = request.args.get('page', 1, type=int)
        category = Category.query.filter(Category.cname == cname).first()
        pagination = Post.query.filter(Post.category_id == category.cid).order_by(Post.time.desc()).paginate(page=page,
                                                                                                             per_page=5)
        posts = pagination.items
        title = '博客分类~{}'.format(category.cname)
        url = url_for('blog.category', cname=cname)
        return render_template('blog/category.html', posts=posts, pagination=pagination, title=title, url=url)
    except Exception as e:
        title = '没有该分类，或者被删除'
        print(e)
        return render_template('blog/base.html', title=title)


@blog.route('/tag/<string:tname>/')
def tag(tname):
    try:
        page = request.args.get('page', 1, type=int)
        tag = Tag.query.filter(Tag.tname == tname).first()
        pagination = Post.query.filter(Post.tag_id == tag.tid).order_by(Post.time.desc()).paginate(page=page,
                                                                                                   per_page=5)
        posts = pagination.items
        title = '博客标签~{}'.format(tag.tname)
        url = url_for('blog.tag', tname=tname)
        return render_template('blog/category.html', posts=posts, pagination=pagination, title=title, url=url)
    except Exception as e:
        title = '没有该标签，或者被删除'
        print(e)
        return render_template('blog/base.html', title=title)


@blog.route('/post/<int:p>/')
def post(p):
    try:
        posts = Post.query.filter(Post.pid == p).first()
        return render_template('blog/post.html', posts=posts)
    except:
        title = '没有该文章，或者被删除'
        return render_template('blog/base.html', title=title)


@blog.route('/search/', methods=['GET', 'POST'])
def search():
    if request.args.get('info'):
        info = request.args.get('info')
    else:
        info = request.form.get('info')
    try:
        if not info is None:
            results = Post.query.filter(Post.title.like('%{}%'.format(info)))
        else:
            error = '搜索不能为空'
            return render_template('blog/base.html', title=error)
    except:
        return redirect(url_for('search'))
    page = request.args.get('page', 1, int)
    pagination = results.paginate(page=page, per_page=10, error_out=False)
    records = pagination.items
    return render_template('blog/search.html', records=records, pagination=pagination, info=info)
