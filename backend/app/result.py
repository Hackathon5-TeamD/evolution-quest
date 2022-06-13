from flask import Blueprint

result_module = Blueprint("result", __name__)

@result_module.route("/result/")
def result():
    return "result test" 