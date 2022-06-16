import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from flask_migrate import Migrate

# appにおいておくと循環エラー出るのでこちらに
app = Flask(__name__)

base_dir = os.path.dirname(__file__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "data.sqlite"
)

# 使用しない機能と思うため,また明示的にオフしておかないとエラーが出ることがある
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app, db)

# 以降各テーブル usersテーブルのクラス名はUserだとザックリしすぎなのでPersonとした
class Person(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255))
    password = db.Column(db.String(255))

class Terminologie(db.Model):
    __tablename__ = "terminologies"
    
    terminologie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_id = db.Column(db.Integer)
    theme_jp = db.Column(db.String(255))
    theme_ro = db.Column(db.String(255))
    description_ja = db.Column(db.Text)
    description_ro = db.Column(db.Text)
<<<<<<< HEAD

class Genre(db.Model):
    __tablename__ ="genres"
    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre = db.Column(db.String(255))
=======
    
>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b

# 小数点以下が入るとのことでaccuracy_valueとwpmをFloatに変更
class Result(db.Model):
    __tablename__ = "results"
    
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
<<<<<<< HEAD
    user_id = db.Column(db.Integer)
    accuracy_value = db.Column(db.Float)
    wpm = db.Column(db.Float)
    playd_at_date = db.Column(db.String(255))
=======
    user_id = db.Column(db.Integer)#forリンキー
    accuracy_value = db.Column(db.Integer)
    wpm = db.Column(db.String)
    playd_at_date = db.Column(db. String)
    # playd_at_date = db.Column(db.DateTime,default=datetime.now(pytz.timezone('Asia/Tokyo'))
    
db.create_all()
>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b
