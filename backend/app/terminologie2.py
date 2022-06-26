from flask import Blueprint, jsonify
from model import app
import random

app.config["JSON_AS_ASCII"] = False

terminologie_module = Blueprint("terminologie_module", __name__)
terminologie_module2 = Blueprint("terminologie_module2", __name__)
create_module = Blueprint("create_module", __name__, template_folder="templates")
update_module = Blueprint("update_module", __name__, template_folder="templates")
delete_module = Blueprint("delete_module", __name__)

# 用語全てからランダムで問題をJSONで取得
@terminologie_module2.route("/terminologie2/", methods=["GET"])
def terms():
    data = [
        {
            "terminologie_id": 1,
            "genre_id": 1,
            "theme_jp": "WEB三層とは",
            "theme_ro": "WEBsansoutoha",
            "description_ja": "クライアントからの処理をするサーバーが、プレゼンテーション層・アプリケーション層・データベース層の3層から構成されているため、Web3層構造と呼びます。",
            "description_ro": "kuraiantokaranosyoriwosurusa-ba-"
        },
        {
            "terminologie_id": 2,
            "genre_id": 2,
            "theme_jp": "WEB三層とは",
            "theme_ro": "WEBsansoutoha",
            "description_ja": "クライアントからの処理をするサーバーが、プレゼンテーション層・アプリケーション層・データベース層の3層から構成されているため、Web3層構造と呼びます。",
            "description_ro": "kuraiantokaranosyoriwosurusa-ba-"
        }
    ]
    
    return(random.choice(data))
        

# # 用語を１つだけJSONで取得
# @terminologie_module.route("/terminologie/<int:terminologie_id>", methods=["GET"])
# def term(terminologie_id):
#     term = Terminologie.query.get(terminologie_id)
#     data = [
#     {
#         "terminologie_id": term.terminologie_id,
#         "genre_id": term.genre_id,
#         "theme_jp": term.theme_jp,
#         "theme_ro": term.theme_ro,
#         "description_ja": term.description_ja,
#         "description_ro": term.description_ro
#     }
#     ]
#     return jsonify(data) 

# # 用語の新規作成
# @create_module.route("/create", methods=["GET", "POST"])
# def create():
#     if request.method == "POST":
#         genre_id = request.form.get("genre_id")
#         theme_jp = request.form.get("theme_jp")
#         theme_ro = request.form.get("theme_ro")
#         description_ja = request.form.get("description_ja")
#         description_ro = request.form.get("description_ro")
        
#         post = Terminologie(genre_id=genre_id, theme_jp=theme_jp, theme_ro=theme_ro, description_ja=description_ja, description_ro=description_ro)
        
#         # 新規データなのでadd必要
#         db.session.add(post)
#         db.session.commit()
#         return redirect("/create")
#     else:
#         return render_template("create.html")
    
# # 用語の編集
# @update_module.route("/update/<int:terminologie_id>", methods=["GET", "POST"])
# def update(terminologie_id):
#     term = Terminologie.query.get(terminologie_id)
#     if request.method == "GET":
#         return render_template("update.html", term=term)
#     else:
#         term.genre_id = request.form.get("genre_id")
#         term.theme_jp = request.form.get("theme_jp")
#         term.theme_ro = request.form.get("theme_ro")
#         term.description_ja = request.form.get("description_ja")
#         term.description_ro = request.form.get("description_ro")
                
#         db.session.commit()
#         return "用語の編集が完了しました"

# # 用語の削除（問答無用で削除されます）
# @delete_module.route("/delete/<int:terminologie_id>", methods=["GET", "POST"])
# # @login_required
# def delete(terminologie_id):
#     post = Terminologie.query.get(terminologie_id)
    
#     db.session.delete(post)
#     db.session.commit()
#     return "用語が削除されました"