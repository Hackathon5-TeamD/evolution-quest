
from flask import Blueprint, request , jsonify
from model import Person, db, app
from flask_bcrypt import generate_password_hash, check_password_hash 
# from flask_login import UserMixin, login_user
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data.sqlite')  # data.sqliteというデータベースを使うという宣言です
Base = declarative_base()  # データベースのテーブルの親です

Base.metadata.create_all(engine)  # 実際にデータベースを構築します
SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路です
session = SessionMaker()  # 経路を実際に作成しました
 

app.config["JSON_AS_ASCII"] = False

user_module = Blueprint("user_module", __name__, url_prefix="/person")

# User全てをJSONで取得
@user_module.route("", methods=["GET"])
def user():
    persons = Person.query.all()
    data = [
        {
            "id": i.id,
            "user_name": i.user_name,
            "password": i.password
        }
        for i in persons
    ]
    return jsonify(data) 
#sign-upの機能
@user_module.route('',methods=["POST"])
def post_user():
    payload = request.json
    insert_data = Person(
        user_id = payload.get("user_id"),
        user_name = payload.get("user_name"),
        password = generate_password_hash(payload.get("password"))
        )

    db.session.add(insert_data)
    db.session.commit()
    return payload # mainページに飛ぶ

@user_module.route('/login',methods=["GET","POST"])
def login_user():
    payload = request.json
    insert_data = Person(
        user_id = payload.get("user_id"),
        user_name = payload.get("user_name"),
        password = payload.get("password"))
    
    user = Person.query.filter_by(user_name=insert_data.user_name).first()
    if check_password_hash(user.password, insert_data.password):
        username = session.query(Person).get("user_id")
        # return  jsonify([{"user_name":user.user_name}])
        return {
                "user_name":user.user_name
               }        
    else:
        return "nameかpass違うよ"
    