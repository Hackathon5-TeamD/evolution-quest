from flask import Flask

# モジュールのインポート
from user import user_module
from terminologie import terminologie_module
from result import result_module

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello,World"

# コントローラー先
app.register_blueprint(user_module)
app.register_blueprint(terminologie_module)
app.register_blueprint(result_module)

if __name__ == '__main__':
    app.run()