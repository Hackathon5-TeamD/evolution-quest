from flask import Blueprint, jsonify, redirect, render_template, request
from model import app, Terminologie, db

app.config['JSON_AS_ASCII'] = False

terminologie_module = Blueprint("terminologie_module", __name__)
create_module = Blueprint("create_module", __name__, template_folder="templates")
update_module = Blueprint("update_module", __name__, template_folder="templates")

# 用語全てをJSONで取得
@terminologie_module.route("/terminologie/", methods=["GET"])
def term():
    terms = Terminologie.query.all()
    data = [
        {
            "terminologie_id": i.terminologie_id,
            "genre_id": i.genre_id,
            "theme_jp": i.theme_jp,
            "theme_ro": i.theme_ro,
            "description_ja": i.description_ja,
            "description_ro": i.description_ro
        }
        for i in terms
    ]
    
    return jsonify(data) 

# 用語の新規作成
@create_module.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        genre_id = request.form.get("genre_id")
        theme_jp = request.form.get("theme_jp")
        theme_ro = request.form.get("theme_ro")
        description_ja = request.form.get("description_ja")
        description_ro = request.form.get("description_ro")
        
        post = Terminologie(genre_id=genre_id, theme_jp=theme_jp, theme_ro=theme_ro, description_ja=description_ja, description_ro=description_ro)
        
        # 新規データなのでadd必要
        db.session.add(post)
        db.session.commit()
        return redirect("/create")
    else:
        return render_template("create.html")
    
# 用語の編集
@update_module.route("/update/<int:terminologie_id>", methods=["GET", "POST"])
def update(terminologie_id):
    term = Terminologie.query.get(terminologie_id)
    if request.method == "GET":
        return render_template('update.html', term=term)
    else:
        term.genre_id = request.form.get("genre_id")
        term.theme_jp = request.form.get("theme_jp")
        term.theme_ro = request.form.get("theme_ro")
        term.description_ja = request.form.get("description_ja")
        term.description_ro = request.form.get("description_ro")
                
        db.session.commit()
        return "用語の編集が完了しました"