import os


class BaseConfig(object):

    SECRET_KEY = os.urandom(24)
    DBMS = 'mysql'
    DRIVER = 'pymysql'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask'
    USER = 'root'
    PASSWORD = 'root'
    CHARSET = 'utf8mb4'

    SQL_URL = '{dbms}+{driver}://{username}:{password}@{host}:{port}/{dbname}?charset={char}'. \
        format(dbms=DBMS,
               driver=DRIVER,
               username=USER,
               password=PASSWORD,
               host=HOST,
               port=PORT,
               dbname=DATABASE,
               char=CHARSET)
    SQLALCHEMY_DATABASE_URI = SQL_URL

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass



class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,  # 开发环境
    'testing': TestingConfig,  # 测试环境
    'production': ProductionConfig  # 生产环境
}
