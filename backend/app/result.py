from flask import Blueprint, request, jsonify
from model import Result, db, app, Person


app.config['JSON_AS_ASCII'] = False

result_module = Blueprint("result_module", __name__,url_prefix="/result")

@result_module.route("")
def get_result():
    results = Result.query.all()
    data = [
        {
        "result_id" :i.result_id,
        "user_id" : i.user_id,
        "accuracy_value" : i.accuracy_value,
        "wpm" : i.wpm,
        "played_at_date": i.played_at_date,
        }
        for i in results
    ]
    return jsonify(data) 


#ランキング1~10まで出力

@result_module.route("/1", methods=["GET"])
def get_join_result():
    results = db.session.query(Result, Result.accuracy_value, Result.user_id, Person.user_name, Person.user_id).join(Person,Result.user_id == Person.user_id) 
    data = [
        {
        "user_name" : i.user_name,
        "accuracy_value" : i.accuracy_value,
        }
        for i in results
    ]
    return jsonify(sorted(data, key=lambda x: x['accuracy_value'],reverse=True)[0:10])


#ランキング11~20まで出力
@result_module.route("/2", methods=["GET"])
def get_join_result2():
    results = db.session.query(Result, Result.accuracy_value, Result.user_id, Person.user_name, Person.user_id).join(Person,Result.user_id == Person.user_id) 
    data = [
        {
        "user_name" : i.user_name,
        "accuracy_value" : i.accuracy_value,
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
        played_at_date=payload.get("played_at_date"),
    )
    db.session.add(insert_data)
    db.session.commit()
    return payload
