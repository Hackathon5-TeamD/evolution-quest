<<<<<<< HEAD
from flask import Blueprint, jsonify
from model import Person, app

app.config['JSON_AS_ASCII'] = False

user_module = Blueprint("user_module", __name__, url_prefix="/user")

# User全てをJSONで取得
@user_module.route("/")
=======
from flask import Blueprint, request, jsonify
from model import Person, db, app
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

# user_module = Blueprint("user_module", __name__)
# ma = Marshmallow(app)

app.config['JSON_AS_ASCII'] = False

user_module = Blueprint("user_module", __name__, url_prefix="/user")

# User全てをJSONで取得
@user_module.route("")
>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b
def user():
    persons = Person.query.all()
    data = [
        {
<<<<<<< HEAD
            "id": i.id,
=======
            "user_id": i.user_id,
>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b
            "user_name": i.user_name,
            "password": i.password
        }
        for i in persons
    ]
    
<<<<<<< HEAD
    return jsonify(data) 
=======
    return jsonify(data) 

@user_module.route('',methods=["POST"])
def post_user():
    payload = request.json
    insert_data = Person(
        user_id = payload.get("user_id"),
        user_name = payload.get("user_name"),
        password = payload.get("password")
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



>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b
