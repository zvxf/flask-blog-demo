# 使用flask编写的blog
###### 练习项目，不再更新。
###### blog-demo   **只是简单的使用**，不再说明。

### blog-demo-rc  

###### `wsgi.py         作为入口文件`

###### `app             目录包含所有代码`

###### `static          静态目录`

###### `templates       模板目录`

###### `views           蓝图文件`

###### `__init__.py     初始化文件，加载配置，创建app`

###### `config.py       连接数据库的配置，mysql，`

###### `forms.py        FlaskForm表单文件`

###### `model.py        数据库表,实现一对多`

------

###### *使用的技术有*

###### *flask_sqlalchemy (pymysql作为启动，使用数据库为mysql8，需要改成mysql5的配置，mysql_native_password)*

###### *flask_login      (实现登录，注册)*

###### *Blueprint        (blog页面，文章页面，增删改查页面，注册登录页面等)*

###### *amazeui          (ui框架，页面布局)***