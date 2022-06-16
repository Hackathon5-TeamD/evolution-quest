<<<<<<< HEAD
from model import app
=======
from model import   app#, Person, db
# from flask import request
>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b

# # モジュールのインポート
from main import main_module
from user import user_module
from terminologie import terminologie_module, create_module, update_module, delete_module
from result import result_module

<<<<<<< HEAD
# # コントローラー先
=======
# app = Flask(__name__)

# コントローラー先
>>>>>>> 0b0ce77b8cd3479e38ac10ff1e521a21c50c084b
app.register_blueprint(main_module)
app.register_blueprint(user_module)
app.register_blueprint(terminologie_module)
app.register_blueprint(create_module)
app.register_blueprint(update_module)
app.register_blueprint(delete_module)
app.register_blueprint(result_module)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)