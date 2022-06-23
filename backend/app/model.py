from audioop import cross
import os
from unittest import result
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 使用していないと思われるため一旦コメントアウト
# import pytz

from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


base_dir = os.path.dirname(__file__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('MYSQL_USER'),
      'password': os.getenv('MYSQL_PASSWORD'),
      'host': os.getenv('MYSQL_HOST'),
      'port': os.getenv("MYSQL_PORT"),
      'database': os.getenv('MYSQL_DATABASE'),
    })
  
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
#     base_dir, "data.sqlite"
# )
#jwtとの関係があるのかな？いらない？
#session情報の暗号化？
app.config['SECRET_KEY'] = os.urandom(24)

# 使用しない機能と思うため,また明示的にオフしておかないとエラーが出ることがある
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app, db)

# 以降各テーブル usersテーブルのクラス名はUserだとザックリしすぎなのでPersonとした
class Person(UserMixin,db.Model):
    
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    
    
    result= db.relationship("Result", backref="users")

class Terminologie(db.Model):
    __tablename__ = "terminologies"
    
    terminologie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_id = db.Column(db.Integer)
    theme_jp = db.Column(db.String(255))
    theme_ro = db.Column(db.String(255))
    description_ja = db.Column(db.Text)
    description_ro = db.Column(db.Text)
    
class Genre(db.Model):
    __tablename__ ="genres"
    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre = db.Column(db.String(255))

# 小数点以下が入るとのことでaccuracy_valueとwpmをFloatに変更
class Result(db.Model):
    __tablename__ = "results"
    
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id')) #user_idからidに修正
    accuracy_value = db.Column(db.Float)
    wpm = db.Column(db.Float)
    playd_at_date = db.Column(db. String(255))
    
    
    # def result_user():
    #     return SELECT * FROM users CROSS JOIN results;