from flask import Blueprint #, render_template

main_module = Blueprint("main", __name__)

@main_module.route("/")
def index():
    return "<h1>Hello,World</h1>"
    # return render_template("index.html")