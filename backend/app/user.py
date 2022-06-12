from flask import Blueprint, jsonify
from model import Person, app

app.config['JSON_AS_ASCII'] = False

user_module = Blueprint("user_module", __name__, url_prefix="/user")

@user_module.route("/")
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