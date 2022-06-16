import bcrypt
from flask import Blueprint, request, jsonify
from model import Person, db, app
from flask_bcrypt import generate_password_hash, check_password_hash#, Bcrypt

# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

# user_module = Blueprint("user_module", __name__)
# ma = Marshmallow(app)
# bcrypt = Bcrypt(app)
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


# class UserSchema(ma.Schema):   
#     class Meta:    
#         fields = ('id','user_name','password')


# user_schema = UserSchema()
# users_schema = UserSchema(many=True)


# @user_module.route("/user", methods=["GET"])
# def get_user():
#    all_users = Person.query.all()

#    return users_schema.jsonify(all_users)



