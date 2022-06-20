
from flask import Blueprint, request , jsonify
from model import Person, db, app
from flask_bcrypt import generate_password_hash, check_password_hash 
from flask_login import login_user

app.config['JSON_AS_ASCII'] = False

user_module = Blueprint("user_module", __name__, url_prefix="/user")

# User全てをJSONで取得
@user_module.route("")
def user():
    persons = Person.query.all()
    data = [
        {
            "user_id": i.user_id,
            "user_name": i.user_name,
            "password": i.password
        }
        for i in persons
    ]
    return jsonify(data) 
#sign-upの機能
@user_module.route('',methods=["POST"])
def post_user():
    payload = request.json
    insert_data = Person(
        user_id = payload.get("user_id"),
        user_name = payload.get("user_name"),
        password = generate_password_hash(payload.get("password"),method='sha256')
        )

    db.session.add(insert_data)
    db.session.commit()
    return payload # mainページに飛ぶ

@user_module.route('/login',methods=["GET","POST"])

def login_user():
    payload = request.json
    insert_data = Person(
        # user_id = payload.get("user_id"),
        user_name = payload.get("user_name"),
        password = payload.get("password"))
    
    user = Person.query.filter_by(user_name=insert_data.user_name).first()
    if check_password_hash(user.password, insert_data.password):
        return jsonify(payload)
        # login_user(user)
        # return "loginしたよ"
        # return login_user(user)
    else:
        return "nameかpass違うよ"
    


