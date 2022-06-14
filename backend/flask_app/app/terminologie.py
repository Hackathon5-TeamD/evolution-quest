from flask import Blueprint, jsonify
from model import app, Terminologie

app.config['JSON_AS_ASCII'] = False

terminologie_module = Blueprint("terminologie_module", __name__)

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