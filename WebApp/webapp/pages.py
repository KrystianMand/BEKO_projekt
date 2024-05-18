from flask import Blueprint, render_template, request

bp = Blueprint("pages", __name__)

test_animations = {'First': 'First content', 'Second': 'Secondcontent'}

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/animations", methods=['GET', 'POST'])
def animations():
    if request.method == 'GET':
        return render_template("pages/animations.html", animations=test_animations)

    elif request.method == 'POST':
        message = "Animation sent!"
        return render_template("pages/animations.html", animations=test_animations, message=message)
        