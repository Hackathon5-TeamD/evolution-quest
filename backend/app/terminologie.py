from flask import Blueprint

terminologie_module = Blueprint("terminologie", __name__)

@terminologie_module.route("/terminologie", methods=["GET"])
def terminologie():
    return "terminologie test"