<<<<<<< HEAD
from flask import Blueprint, jsonify
from model import app, Result

app.config['JSON_AS_ASCII'] = False
=======
from flask import Blueprint, request, jsonify
from model import Result, db, app
>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b

app.config['JSON_AS_ASCII'] = False

<<<<<<< HEAD
# 用語全てをJSONで取得
@result_module.route("/result/", methods=["GET"])
def result():
    results = Result.query.all()
    data = [
        {
            "result_id": i.result_id,
            "user_id": i.user_id,
            "accuracy_value": i.accuracy_value,
            "wpm": i.wpm,
            "playd_at_date": i.playd_at_date,
        }
        for i in results
    ]
    
    return jsonify(data) 
=======
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
        "playd_at_date": i.playd_at_date,
        }
        for i in results
    ]
    return jsonify(data) 

#直近の5日分出力
@result_module.route("/user")
def get_my_result():
    results = Result.query.all()
    data = [
        {
        # "result_id" :i.result_id,
        # "user_id" : i.user_id,
        "accuracy_value" : i.accuracy_value,
        "wpm" : i.wpm,
        "playd_at_date": i.playd_at_date,
        }
        for i in results
    ]
    return jsonify(sorted(data, key=lambda x: x['playd_at_date'],reverse=True)[0:5])

#ランキングトップ１０
@result_module.route("/1")
def get_result_1():
    results = Result.query.all()
    data = [
        {
        # "result_id" :i.result_id,
        # "user_id" : i.user_id,
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
    data = [
        {
        # "result_id" :i.result_id,
        # "user_id" : i.user_id,
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
>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b
