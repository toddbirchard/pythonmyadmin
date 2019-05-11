import os
from flask import Blueprint, render_template
from flask_assets import Environment, Bundle
from flask import current_app as app

# Create Blueprint
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

# Configure Flask-Assets
assets = Environment(app)
Environment.auto_build = True
Environment.debug = False
less_bundle = Bundle('less/*.less',
                     filters='less,cssmin',
                     output='dist/css/plotly-flask-tutorial.css',
                     extra={'rel': 'stylesheet/less'})
js_bundle = Bundle('js/*.js',
                   filters='jsmin',
                   output='dist/js/main.js')
assets.register('less_all', less_bundle)
assets.register('js_all', js_bundle)
if app.config['FLASK_ENV'] == 'development':
    less_bundle.build(force=True)
    js_bundle.build()


# Landing Page
@main_bp.route('/', methods=['GET'])
def home():
    """Database Table Selection Page."""
    return render_template('index.html',
                           title='Plotly Flask Tutorial.',
                           template='home-template',
                           body="This is an example homepage, served with Flask.")


@main_bp.route('/database', methods=['GET'])
def database():
    """Database Table Selection Page."""
    return render_template('index.html',
                           title='Simple DB.',
                           template='home-template',
                           body="This is an example homepage, served with Flask.")


@main_bp.route('/users', methods=['GET'])
def users():
    """Database Table Selection Page."""
    return render_template('index.html',
                           title='Users.',
                           template='users-template',
                           body="This is an example homepage, served with Flask.")


@main_bp.route('/settings', methods=['GET'])
def settings():
    """Database Table Selection Page."""
    return render_template('index.html',
                           title='Settings.',
                           template='settings-template',
                           body="This is an example homepage, served with Flask.")
