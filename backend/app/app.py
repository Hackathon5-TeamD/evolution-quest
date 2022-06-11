from model import Person, db, app
from flask import request

# モジュールのインポート
from main import main_module
from user import user_module
from terminologie import terminologie_module
from result import result_module

# app = Flask(__name__)

# コントローラー先
app.register_blueprint(main_module)
app.register_blueprint(user_module)
app.register_blueprint(terminologie_module)
app.register_blueprint(result_module)

@app.route('/user',methods=["POST"])
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
   


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)