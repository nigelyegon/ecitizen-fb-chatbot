from flask import Flask
from config import config
from extensions import jwt
from .models import RevokedToken


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    register_blueprints(app)
    initialize_extensions(app)
    return app


# ---------------------------------------------
# helper functions
# ---------------------------------------------
def initialize_extensions(app):
    from extensions import db, migrate, bcrypt, cors

    db.init_app(app)
    with app.app_context() as context:
        context.push()
        db.create_all()
    migrate.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)


def register_blueprints(app):
    from .api.auth.views import auth_blueprint
    from .api.facebook_api.views import facebook_api_bp
    from .api.dashboard.views import dashboard_bp

    # Auth blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/api/v1/chatbot")
    # Facebook webhook blueprint
    app.register_blueprint(facebook_api_bp, url_prefix="/api/v1/chatbot")
    # Dashboard blueprint
    app.register_blueprint(dashboard_bp, url_prefix="/api/v1/chatbot")


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(self, decrypt_token):
    jti = decrypt_token["jti"]
    return RevokedToken.is_token_blacklisted(jti)
