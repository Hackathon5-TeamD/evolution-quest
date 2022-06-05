from flask import Blueprint

user_module = Blueprint("user_module", __name__)

@user_module.route("/user/")
def user():
    return "user test" 