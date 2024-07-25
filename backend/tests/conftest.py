import pytest
from app import create_app
from extensions import db as _db
import os

config_mode = os.environ["CONFIG_MODE"]


@pytest.fixture(scope="session")
def app():
    # app setup
    app = create_app(config_mode)
    with app.app_context():
        # create all test tables
        _db.create_all()

        yield app

        # app teardown
        _db.session.remove()
        if "test" in app.config["SQLALCHEMY_DATABASE_URI"]:
            # drop all test tables
            _db.drop_all()


@pytest.fixture(scope="function")
def test_client(app):
    return app.test_client()
