import os


class Config:
    # SQLALCHEMY_TRACK_MODIFICATIONS:
    # A configuration to enable or disable tracking modifications of objects.
    # You set it to False to disable tracking and use less memory
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ["DEVELOPMENT_DATABASE_URL"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    JWT_TOKEN_LOCATION = os.environ["JWT_TOKEN_LOCATION"]


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]


class TestingConfig(Config):
    Testing = True
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
    SQLALCHEMY_DATABASE_URI = os.environ["TEST_DATABASE_URL"]


class StagingConfig(Config):
    DEVELOPMENT = True


class ProductionConfig(Config):
    PRODUCTION = True
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}
