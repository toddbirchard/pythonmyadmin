"""Build static assets."""

from flask import Flask
from flask_assets import Bundle, Environment


def compile_js_assets(app: Flask):
    """Build JS bundle."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    js_bundle = Bundle("js/*.js", filters="jsmin", output="dist/js/main.js")
    assets.register("js_all", js_bundle)
    js_bundle.build()


def compile_style_assets(app: Flask):
    """Build CSS style bundle."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    less_bundle = Bundle(
        "less/main.less",
        filters="less,cssmin",
        output="dist/css/style.css",
        extra={"rel": "stylesheet/less"},
    )
    assets.register("less_all", less_bundle)
    less_bundle.build(force=True)
