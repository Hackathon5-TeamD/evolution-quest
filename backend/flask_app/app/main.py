# from flask import Blueprint
from flask import Blueprint, jsonify, redirect, render_template, request


main_module = Blueprint("main", __name__)

@main_module.route("/")
def index():
    return "<h1>Hello,World135</h1>"
    # return render_template("index.html")