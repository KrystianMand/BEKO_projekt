from flask import Blueprint
from webapp.models import AnimationsModel

bp = Blueprint("endpoints", __name__)

@bp.route("/endpoints/animations/<int:id>")
def endpoints_animations(id):
    animation = AnimationsModel.query.get(id)
    if animation is None:
        return {"error": "Animation not found"}, 404
    else:
        return {
            "id": animation.id,
            "name": animation.name,
            "rgb_values": animation.rgb_values
        }
