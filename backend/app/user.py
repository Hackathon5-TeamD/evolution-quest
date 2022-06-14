from flask import Blueprint, request, jsonify
from model import Person, db, app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

user_module = Blueprint("user_module", __name__)
ma = Marshmallow(app)
# @user_module.route("/user/")
# def get_user():
#     users = Person.query.get(1)
#     # data = {
#     #     id = "id",
#     # }
#     return jsonify(users)
    # return "user test" 

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


class UserSchema(ma.Schema):   
    class Meta:    
        fields = ('id','user_name','password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_module.route("/user", methods=["GET"])
def get_user():
   all_users = Person.query.all()

   return users_schema.jsonify(all_users)


# print(Person.query.first())
