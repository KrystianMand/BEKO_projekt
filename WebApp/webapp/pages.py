import json
from flask import Blueprint, render_template, request
from webapp.models import GatewaysModel, AnimationsModel

ANIMATIONS_JSON_PATH = 'webapp/resources/animations.json'

bp = Blueprint("pages", __name__)

test_animations = {'First': 'First content', 'Second': 'Secondcontent'}

# with open(ANIMATIONS_JSON_PATH, 'r') as f:
#     test_animations = json.load(f)

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

@bp.route("/gateways", methods=['GET', 'POST'])
def gateways():
    if request.method == 'GET':
        gateways = GatewaysModel.query.all()
        print(gateways)
        gateways = [
            {
                "id": gateway.id,
                "ip": gateway.ip,
                "location": gateway.location
            } for gateway in gateways]
        
        return render_template("pages/gateways.html", gateways=gateways)

    elif request.method == 'POST':
        selected_gateways = [key for key in request.form.keys() if key.startswith('gateway_')]
        selected_gateways_ids = [request.form[key] for key in selected_gateways]

        return render_template("pages/gateways.html")
        