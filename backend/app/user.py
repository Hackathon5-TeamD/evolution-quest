from flask import Blueprint
from model import Person, db, app

user_module = Blueprint("user_module", __name__)

# @user_module.route("/user/")
# def user():
#     return "user test" 
@app.route('/user')
def get_user():
    
    payload = request.json
    insert_data = Person(
        id = payload.get("id"),
        user_name = payload.get("user_name"),
        password = payload.get("password")
    )
    db.session.add(insert_data)
    db.session.commit()
    return payload
   