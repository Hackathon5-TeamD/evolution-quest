from flask import Blueprint

terminologie_module = Blueprint("terminologie_module", __name__)

@terminologie_module.route("/terminologie/", methods=["GET"])
def term():
    return "Terminologie test"