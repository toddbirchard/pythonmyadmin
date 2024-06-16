"""Flask app configuration."""

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Global configuration variables."""

    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    ENVIRONMENT = environ.get("ENVIRONMENT")
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_HOST = environ.get("SQLALCHEMY_DATABASE_HOST")
    SQLALCHEMY_DATABASE_TABLE = environ.get("SQLALCHEMY_DATABASE_TABLE")
    SQLALCHEMY_DATABASE_NAME = environ.get("SQLALCHEMY_DATABASE_NAME")
    SQLALCHEMY_CONNECT_ARGS = {"ssl": {"ca": "./creds/ca-certificate.crt"}}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Assets
    LESS_BIN = environ.get("LESS_BIN")
    ASSETS_DEBUG = environ.get("ASSETS_DEBUG")
    LESS_RUN_IN_DEBUG = environ.get("LESS_RUN_IN_DEBUG")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")
