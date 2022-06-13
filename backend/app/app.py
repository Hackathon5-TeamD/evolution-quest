from model import   app#, Person, db
# from flask import request

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)