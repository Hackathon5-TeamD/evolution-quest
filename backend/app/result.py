from flask import Blueprint, request
from model import Result, db

result_module = Blueprint("result", __name__)

# @result_module.route("/result/")
# def result():
#     return "result test" 

@result_module.route("/result",methods=["POST"])
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