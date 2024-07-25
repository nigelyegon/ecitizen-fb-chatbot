from flask import Flask
from config import config


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
    from extensions import db, migrate

    db.init_app(app)
    with app.app_context() as context:
        context.push()
        db.create_all()
    migrate.init_app(app)


def register_blueprints(app):
    from .api.auth.views import auth_blueprint
    from .api.facebook_api.views import facebook_api_bp
    from .api.dashboard.views import dashboard_bp

    # Auth blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/api/v1")
    # Facebook webhook blueprint
    app.register_blueprint(facebook_api_bp, url_prefix="/api/v1")
    # Dashboard blueprint
    app.register_blueprint(dashboard_bp, url_prefix="/api/v1")
