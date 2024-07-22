from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        from . import routes, models
        from .dashboard import dashboard_bp  # dashboard route 
        app.register_blueprint(dashboard_bp, url_prefix='/dashboard') 
        db.create_all()
        
    return app
