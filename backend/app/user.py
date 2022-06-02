from flask import Blueprint

user_module = Blueprint("user", __name__)

@user_module.route("/user", methods=["GET"])
def user():
    return "user test" 