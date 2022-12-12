from flask import Blueprint, render_template


Admin = Blueprint("admin", __name__)

@Admin.route("/")
def index():
    return render_template("dashboard.html")