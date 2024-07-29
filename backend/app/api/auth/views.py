from flask import Blueprint, request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt,
    create_refresh_token,
    get_jwt_identity,
)
from sqlalchemy import exc
from app.models import User, RevokedToken


auth_blueprint = Blueprint("auth_blueprint", __name__)


@auth_blueprint.route("/auth/register", methods=["POST"])
def register():
    req = request.get_json()
    password = req.get("password")
    email = req.get("email")
    user = User(email=email, password=User.generate_hash(password))
    try:
        if not User.find_user_by_email(email=email):
            user.save()
            return {"message": "User created successfully", "status_code": 201}, 201
        return {"message": "User already exists", "status_code": 409}, 409

    except exc.IntegrityError as e:
        user.undo()
        return {"message": e.orig.args[1], "status_code": 400}, 400


@auth_blueprint.route("/auth/login", methods=["POST"])
def login():
    req = request.get_json()
    password = req.get("password")
    email = req.get("email")
    user = User.find_user_by_email(email)
    try:
        if user:
            if User.verify_hash(user.password, password):
                token = create_access_token(identity=email, fresh=True)
                refresh = create_refresh_token(identity=email)

                return {
                    "message": "User authentication successful",
                    "status_code": 200,
                    "access_token": token,
                    "refresh_token": refresh,
                }, 200
        return {"message": "Wrong login credentials!", "status_code": 401}, 401

    except exc.IntegrityError as e:
        User.undo()
        return {"message": e.orig.args[1], "status_code": 400}, 400


@auth_blueprint.route("/auth/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    try:
        RevokedToken(jti=jti).save()

        return {"message": "logout successful", "status_code": 200}, 200
    except Exception as e:
        return {"message": "Error"}, 400


@auth_blueprint.route("/auth/refresh", methods=["POST"])
@jwt_required(refresh=True)
def get_refresh_tokens():
    current_user = get_jwt_identity()
    try:
        return {
            "access_token": create_access_token(identity=current_user, fresh=False),
            "status_code": 200,
        }, 200
    except Exception as e:
        return {"message": "Error"}, 400
