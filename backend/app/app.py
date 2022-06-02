# from backend import create_app

# app = create_app()

# if __name__ =='__main__':
#     app.run(debug=True)

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# login_manager = LoginManager()
# login_manager.login_view = 'app.login'
# login_manager.login_message = 'ログインしてください'


base_dir = os.path.abspath(os.path.dirname(__name__))

db = SQLAlchemy()
# migrate = Migrate()


app = Flask(__name__)
@app.route('/')
def create_app():
    
    # app.config['SEKRET_KEY'] = 'mysite'
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, 'data.sqlite')
    # # 使用しない機能と思うため,また明示的にオフしておかないとエラーが出ることがある
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # from backend.app.views import bp
    # app.register_blueprint(bp)
    # db.init_app(app)
    # migrate.init_app(app, db)
    # login_manager.init_app(app)
    return " hello world"

# app = create_app()

if __name__ =='__main__':
    app.run()
