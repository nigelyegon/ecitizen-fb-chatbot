from flask import Blueprint, request, make_response
from sqlalchemy import exc
from extensions import db

from app.models import User


auth_blueprint = Blueprint("auth_blueprint", __name__)


@auth_blueprint.route("/auth/register", methods=["POST"])
def register():
    req = request.get_json()
    user = User(email=req.get("email"), password=req.get("password"))
    try:
        db.session.add(user)
        db.session.commit()
        return make_response(
            {"message": "User created successfully", "code": 201}, 201
        )

    except exc.IntegrityError as e:
        db.session.rollback()
        return make_response({"message": e.orig.args[1], "code": 400}, 400)
