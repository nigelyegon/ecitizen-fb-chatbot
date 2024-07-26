from flask import Blueprint, request, make_response
from sqlalchemy import exc
from extensions import db, bcrypt

from app.models import User


auth_blueprint = Blueprint("auth_blueprint", __name__)


@auth_blueprint.route("/auth/register", methods=["POST"])
def register():
    req = request.get_json()
    pswd = req.get("password")
    hashed_password = bcrypt.generate_password_hash(pswd).decode("utf-8")
    email = req.get("email")
    user = User(email=email, password=hashed_password)
    try:
        db.session.add(user)
        db.session.commit()
        return make_response({"message": "User created successfully", "code": 201}, 201)

    except exc.IntegrityError as e:
        db.session.rollback()
        return make_response({"message": e.orig.args[1], "code": 400}, 400)


@auth_blueprint.route("/auth/login", methods=["POST"])
def login():
    req = request.get_json()
    password = req.get("password")
    email = req.get("email")
    try:
        user = User.query.where(User.email == email).first()

        if user:
            if bcrypt.check_password_hash(user.password, password):

                return make_response(
                    {"message": "User authentication successful", "code": 200}, 200
                )
        return make_response({"message": "Wrong login credentials!", "code": 401}, 401)

    except exc.IntegrityError as e:
        db.session.rollback()
        return make_response({"message": e.orig.args[1], "code": 400}, 400)
