from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        # Create tables for our models
        db.create_all()

        # Construct the data set
        from . import routes
        app.register_blueprint(routes.main_bp)

        # Compile assets
        from .assets import compile_assets
        compile_assets(app)

        # Dash view
        from table import tableview
        app = tableview.Add_Dash(app)

        return app
