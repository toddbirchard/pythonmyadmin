"""Core route declaration."""
from flask import Blueprint, render_template
from flask import current_app as app
from . import db


# Create Blueprint
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def home():
    """Database Table Selection Page."""
    tables = db.engine.table_names()
    host = app.config['SQLALCHEMY_DATABASE_HOST']
    db_name = app.config['SQLALCHEMY_DATABASE_NAME']
    return render_template('index.html',
                           tables=tables,
                           title='Database Tables.',
                           template='home-template',
                           host_name=host,
                           table_summary=f'Displaying {len(tables)} tables found in database {db_name}:')


@main_bp.route('/database')
def database():
    """Database Configuration Page."""
    return render_template('index.html',
                           title='Connect a Database',
                           template='database-template',
                           body="This is an example homepage, served with Flask.")


@main_bp.route('/users')
def users():
    """Users Page."""
    return render_template('index.html',
                           title='Users',
                           template='users-template',
                           body="This is an example homepage, served with Flask.")


@main_bp.route('/settings')
def settings():
    """Settings Page."""
    return render_template('index.html',
                           title='Settings',
                           template='settings-template',
                           body="This is an example homepage, served with Flask.")
