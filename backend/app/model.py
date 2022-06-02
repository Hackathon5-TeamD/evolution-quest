from backend.app.app import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash 
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# 使用しない機能と思うため,また明示的にオフしておかないとエラーが出ることがある
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 以降各テーブル usersテーブルのクラス名はUserだとザックリしすぎなのでPersonとした
#UserMixinはFlask-Loginライブラリを利用するユーザーが持つべきオブジェクトを定義
class User(UserMixin.model):
    __tablename__ = 'users'
    
    id = db.Cloumn(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64))
    password = db.Column(db.String(128))
    
    def __init__(self,username, password):
        self.username = username
        self.password = generate_password_hash(password)#ハッシュ化
        #パスワードがあってるかチェックする
    def validate_password(self, password):
        return check_password_hash(self.password, password)
    
    #ユーザーを追加するためのメソッド
    def add_user(self):
        with db.session.begin(subtransactions=True):
            db.session.add(self)
        db.session.commit()   
    
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
    playd_at_date = db.Column(db.DateTime)