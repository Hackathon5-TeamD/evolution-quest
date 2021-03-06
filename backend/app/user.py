
import os
from flask import Blueprint, request , jsonify
from model import Person, db, app
from flask_bcrypt import generate_password_hash, check_password_hash 
# from flask_login import UserMixin, login_user
# from sqlalchemy.orm import sessionmaker

# from sqlalchemy import create_engine, Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
jwt = JWTManager(app)

# engine = create_engine('sqlite:///data.sqlite')  # data.sqliteというデータベースを使うという宣言です
# Base = declarative_base()  # データベースのテーブルの親です

# Base.metadata.create_all(engine)  # 実際にデータベースを構築します
# SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路です
# session = SessionMaker()  # 経路を実際に作成しました
 

app.config["JSON_AS_ASCII"] = False

user_module = Blueprint("user_module", __name__, url_prefix="/user")

# User全てをJSONで取得
@user_module.route("")
def get_user():
    persons = Person.query.all()
    data = [
        {
            "user_id": i.user_id,
            "user_name": i.user_name,
            # "password": i.password,
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
        username = db.session.query(Person).get("user_id")
        return {
                "user_name":user.user_name
               } 
        # access_token = create_access_token(identity=user.user_name)
        # return jsonify(access_token=access_token)
    else:
        return "nameかpass違うよ"
        # return jsonify({"msg": "ユーザー名かパスワードが違います"}), 401

# 以下JWTの仕組み
@user_module.route("/token", methods=["POST"])
def token():
    user_name = request.json.get("user_name")
    password = request.json.get("password")
    if user_name != "test" or password != "test":
        return jsonify({"msg": "ユーザー名かパスワードが違います"}), 401

    access_token = create_access_token(identity=user_name)
    return jsonify(access_token=access_token)

@user_module.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200