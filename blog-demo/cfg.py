import os

DEBUG = True
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
           host=HOST, port=PORT,
           dbname=DATABASE,
           char=CHARSET)
SQLALCHEMY_DATABASE_URI = SQL_URL

SQLALCHEMY_TRACK_MODIFICATIONS = False

