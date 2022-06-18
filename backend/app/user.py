
from flask import Blueprint, request, jsonify
from model import Person, db, app
from flask_bcrypt import generate_password_hash, check_password_hash#, Bcrypt

app.config["JSON_AS_ASCII"] = False

user_module = Blueprint("user_module", __name__, url_prefix="/person")

# User全てをJSONで取得
@user_module.route("", methods=["GET"])
def user():
    persons = Person.query.all()
    data = [
        {
            "id": i.id,
            "user_name": i.user_name,
            "password": i.password
        }
        for i in persons
    ]
    return jsonify(data) 

@user_module.route('',methods=["POST"])
def post_user():
    payload = request.json
    insert_data = Person(
        user_id = payload.get("user_id"),
        user_name = payload.get("user_name"),
        password = generate_password_hash(payload.get("password"))
        )

    db.session.add(insert_data)
    db.session.commit()
    return payload

@user_module.route('/login',methods=["POST"])
def login_user():
    payload = request.json
    insert_data = Person(
        # user_id = payload.get("user_id"),
        user_name = payload.get("user_name"),
        password = generate_password_hash(payload.get("password"))
        )
    user = Person.query.filter_by(user_name=payload.get("user_name")).first() and Person.query.filter_by(password= generate_password_hash(payload.get("password")))
    
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return "loginしたよ"
    else:
        return "nameかpass違うよ"
    