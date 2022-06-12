from flask import Blueprint, jsonify
from model import app, Result

app.config['JSON_AS_ASCII'] = False

result_module = Blueprint("result", __name__)

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