"""Initialize app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from log import LOGGER

db = SQLAlchemy()


def create_app() -> Flask:
    """
    Construct the core application.

    :returns: Flask
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from . import routes
        from .assets import compile_js_assets, compile_style_assets
        from .tables import table_view

        # Create tables for our models
        db.create_all()

        # Compile static assets
        compile_js_assets(app)
        compile_style_assets(app)

        # Register App Blueprint
        app.register_blueprint(routes.main_bp)
        app = table_view.create_dash_view(app)

        LOGGER.info("Flask app initialized.")
        return app
