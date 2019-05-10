from flask import Flask, g
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
        from . import dash_view
        dash_app = dash_view.Add_Dash(app)

        app.register_blueprint(routes.main_bp)

        return app
