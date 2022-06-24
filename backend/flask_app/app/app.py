from model import  app #, Person, db

# # モジュールのインポート
from main import main_module
from user import user_module
from terminologie import terminologie_module, create_module, update_module, delete_module
from result import result_module
from record import record_module

# コントローラー先
app.register_blueprint(main_module)
app.register_blueprint(user_module)
app.register_blueprint(terminologie_module)
app.register_blueprint(create_module)
app.register_blueprint(update_module)
app.register_blueprint(delete_module)
app.register_blueprint(result_module)
app.register_blueprint(record_module)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)