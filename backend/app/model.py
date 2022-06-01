from lib2to3.pgen2.pgen import generate_grammar
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(base_dir, 'data.sqlite')

# 使用しない機能と思うためオフまた、明示的にオフしておかないとエラーが出ることがある
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 以降各テーブル usersテーブルのクラス名はUserだとザックリしすぎなのでPersonとした
class Person(db.model):
    __tablename__ = 'users'
    
    id = db.Cloumn(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255))
    password = db.Column(db.Strong(255))
    
class Terminologie(db.model):
    __tablename__ = 'terminologies'
    terminologie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_id = db.Column(db.Integer)
    theme_jp = db.Column(db.String(255))
    theme_ro = db.Column(db.String(255))
    description_ja = db.Column(db.Text)
    description_ro = db.Column(db.Text)
    
class Result(db.model):
    __tablename__ = 'results'
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    accuracy_value = db.Column(db.integer)
    wpm = db.Column(db.integer)
    playd_at_date = db.Column(db.datetime)