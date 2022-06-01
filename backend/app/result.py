from flask import Blueprint

result_module = Blueprint("result", __name__)

@result_module.route("/result", methods=["GET"])
def result():
    return "result test"