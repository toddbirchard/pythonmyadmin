"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
        # Create tables for our models
        db.create_all()

        # Import parts of our application
        from pythonmyadmin import routes
        from pythonmyadmin.assets import compile_js_assets, compile_style_assets
        from table import tableview

        # Register App Blueprint
        app.register_blueprint(routes.main_bp)

        # Compile static assets
        if app.config["ENVIRONMENT"] == "development":
            compile_js_assets(app)
            compile_style_assets(app)

        app = tableview.create_dash_view(app)

        return app
