from flask import Blueprint, request, jsonify
from model import Result, db, app, Person
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base

import datetime

# JST指定
JST = datetime.timezone(datetime.timedelta(hours=+9))

app.config['JSON_AS_ASCII'] = False

result_module = Blueprint("result_module", __name__,url_prefix="/result")

# engine = create_engine('sqlite:///data.sqlite')  # data.sqliteというデータベースを使うという宣言です
# Base = declarative_base()  # データベースのテーブルの親です

# Base.metadata.create_all(engine)  # 実際にデータベースを構築します
# SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路です
# session = SessionMaker()  # 経路を実際に作成しました

@result_module.route("")
def get_result():
    results = Result.query.all()
    data = [
        {
        "result_id" :i.result_id,
        "user_id" : i.user_id,
        "accuracy_value" : i.accuracy_value,
        "wpm" : i.wpm,
        "playd_at_date": datetime.datetime.fromtimestamp(i.playd_at_date, JST)
        }
        for i in results
    ]
    return jsonify(data) 


#ランキング1~10まで出力

@result_module.route("/1", methods=["GET"])
def get_join_result():
    results = db.session.query(Result, Result.accuracy_value, Result.user_id, Result.playd_at_date, Person.user_name, Person.user_id).join(Person,Result.user_id == Person.user_id) 
    data = [
        {
        "user_name" : i.user_name,
        "accuracy_value" : i.accuracy_value,
        "playd_at_date": datetime.datetime.fromtimestamp(i.playd_at_date, JST),
        }
        for i in results
    ]
    return jsonify(sorted(data, key=lambda x: x['accuracy_value'],reverse=True)[0:10])


#ランキング11~20まで出力
@result_module.route("/2", methods=["GET"])
def get_join_result2():
    results = db.session.query(Result, Result.accuracy_value, Result.user_id, Result.playd_at_date, Person.user_name, Person.user_id).join(Person,Result.user_id == Person.user_id) 
    data = [
        {
        "user_name" : i.user_name,
        "accuracy_value" : i.accuracy_value,
        "playd_at_date": datetime.datetime.fromtimestamp(i.playd_at_date),
        }
        for i in results
    ]
    return jsonify(sorted(data, key=lambda x: x['accuracy_value'],reverse=True)[10:20])


#ゲームの結果を登録
@result_module.route("",methods=["POST"])
def post_result():
    payload = request.json
    insert_data = Result(
        result_id = payload.get("result_id"),
        user_id = payload.get("user_id"),
        accuracy_value = payload.get("accuracy_value"),
        wpm =payload.get("wpm"),
        playd_at_date=payload.get("playd_at_date"),
    )
    db.session.add(insert_data)
    db.session.commit()
    return payload
