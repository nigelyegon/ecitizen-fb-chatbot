from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from ..config import Config
from backend.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import routes, models
        from backend.app.dashboard.dashboard import dashboard_bp
        app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
        from .routes import route_bp  # webhook route
        app.register_blueprint(route_bp, url_prefix='/api/v1/')
        db.create_all()

    return app
