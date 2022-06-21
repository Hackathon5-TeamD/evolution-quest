from flask import Blueprint, request, jsonify
from model import Result, db, app, Person

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

app.config['JSON_AS_ASCII'] = False

result_module = Blueprint("result_module", __name__,url_prefix="/result")
engine = create_engine('sqlite:///data.sqlite')  # data.sqliteというデータベースを使うという宣言です
Base = declarative_base()  # データベースのテーブルの親です

Base.metadata.create_all(engine)  # 実際にデータベースを構築します
SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路です
session = SessionMaker()  # 経路を実際に作成しました

@result_module.route("")
def get_result():
    results = Result.query.all()
    data = [
        {
        "result_id" :i.result_id,
        "user_id" : i.user_id,
        "accuracy_value" : i.accuracy_value,
        "wpm" : i.wpm,
        "playd_at_date": i.playd_at_date,
        }
        for i in results
    ]
    return jsonify(data) 

#直近の5日分出力
@result_module.route("/user/<user_id>",methods=["POST"])
def get_my_result(user_id):
        payload = request.json
        insert_data = Result(
            # result_id = payload.get("result_id"),
            user_id = payload.get("user_id"),
            accuracy_value = payload.get("accuracy_value"),
            wpm = payload.get("wpm"),
            playd_at_date = payload.get("playd_at_date"))
    
        users = Result.query.filter_by(user_id=insert_data.user_id).all()
        # username = session.query(Result).all()
        # return {
        #         "user_id":user.user_id,
        #         "accuracy_value":user.accuracy_value,
        #         "wpm":user.wpm,
        #         "playd_at_date":user.playd_at_date
        #        }        
        my_data = [
            {
                "user_id":i.user_id,
                "accuracy_value":i.accuracy_value,
                "wpm":i.wpm,
                "playd_at_date":i.playd_at_date
            }
            for i in users
        ]
        # return jsonify(my_data)
    
        return jsonify(sorted(my_data, key=lambda x: x['playd_at_date'],reverse=True)[0:5])
        
    
    # results = Result.query.all()
    # results = Result.query.filter(Person.user_id == 1)
    # return jsonify(results)
    #  data = [
    #     {
    #     # "result_id" :i.result_id,
    #     "user_id" : i.user_id,
    #     "accuracy_value" : i.accuracy_value,
    #     "wpm" : i.wpm,
    #     "playd_at_date": i.playd_at_date,
    #     }
        # for i in results
    # ]
    
    # user_data = {"user_id":data[0]["user_id"]} #in data.keys()
    
    # return user_data
    # return {
    #              "user_id":user_data
    # }
    # sort_data = jsonify(sorted(data, key=lambda x: x['playd_at_date'],reverse=True)[0:5])
    # if data.user_id:
    #     return sort_data.user_id == 4




#ランキングトップ１０
@result_module.route("/1")
def get_result_1():
    results = Result.query.all()
    data = [
        {
        # "result_id" :i.result_id,
        "user_id" : i.user_id,
        "accuracy_value" : i.accuracy_value,
        "wpm" : i.wpm,
        "playd_at_date": i.playd_at_date,
        }
        for i in results
        
        
        
    ]
    return jsonify(sorted(data, key=lambda x: x['accuracy_value'],reverse=True)[0:10])

#ランキング11~20まで出力
@result_module.route("/2")
def get_result_2():
    results = Result.query.all()
    # person= Person()
    data = [
        {
        # "result_id" :i.result_id,
        "user_id" : i.user_id,
        "accuracy_value" : i.accuracy_value,
        "wpm" : i.wpm,
        "playd_at_date": i.playd_at_date,
        }
        for i in results
    ]
    return jsonify(sorted(data, key=lambda x: x['accuracy_value'],reverse=True)[10:20])

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
