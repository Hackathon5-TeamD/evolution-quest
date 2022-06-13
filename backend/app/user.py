from flask import Blueprint, request
from model import Person, db, app

user_module = Blueprint("user_module", __name__)

@user_module.route("/user/")
def get_user():
    return "user test" 

# def get_user():
#     return request.args.get(Person('user_name'))


@user_module.route('/user',methods=["POST"])
def post_user():
    payload = request.json
    insert_data = Person(
        id = payload.get("id"),
        user_name = payload.get("user_name"),
        password = payload.get("password")
    )
    db.session.add(insert_data)
    db.session.commit()
    return payload