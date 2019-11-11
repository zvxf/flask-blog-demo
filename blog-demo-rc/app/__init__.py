from flask import Flask, render_template
from flask_login import LoginManager

from app.config import config
from app.model import db, User
from app.views.admin import admin
from app.views.auth import auth
from app.views.blog import blog


def create_app(dev_name=None):
    app = Flask(__name__)
    app.config.from_object(config[dev_name])
    db.init_app(app)
    app.register_blueprint(admin)
    app.register_blueprint(auth)
    app.register_blueprint(blog)
    # 注册登录管理
    login_manager = LoginManager()
    # 初始化
    login_manager.init_app(app)
    # 拦截登录，重定向视图
    login_manager.login_view = "login"
    # 登录验证时LoginManger从数据库加载用户
    login_manager.session_protection = "strong"
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))

    return app
