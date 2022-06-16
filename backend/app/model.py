import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager


login_manager = LoginManager()
# login_manager.login_view = 'app.login'
# login_manager.login_message = 'ログインしてください'

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "data.sqlite"
)

# 使用しない機能と思うため,また明示的にオフしておかないとエラーが出ることがある
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app, db)

# 以降各テーブル usersテーブルのクラス名はUserだとザックリしすぎなのでPersonとした
# class Person(UserMixin, db.Model):
class Person(UserMixin,db.Model):
    
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    
    # def __int__(self, password):
    #     self.password = generate_password_hash(password)
        
    # def valiate_password(self,password):
    #     return check_password_hash(self.password,password)


class Terminologie(db.Model):
    __tablename__ = "terminologies"
    
    terminologie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_id = db.Column(db.Integer)
    theme_jp = db.Column(db.String(255))
    theme_ro = db.Column(db.String(255))
    description_ja = db.Column(db.Text)
    description_ro = db.Column(db.Text)
    

class Result(db.Model):
    __tablename__ = "results"
    
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)#forリンキー
    accuracy_value = db.Column(db.Integer)
    wpm = db.Column(db.String)
    playd_at_date = db.Column(db. String)
    # playd_at_date = db.Column(db.DateTime,default=datetime.now(pytz.timezone('Asia/Tokyo'))
    
db.create_all()
