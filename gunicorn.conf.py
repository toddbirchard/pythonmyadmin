"""Gunicorn configuration file."""

from os import environ, path

from dotenv import load_dotenv

# Read environment variables from ".env" file.
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Fetch deployment environment from environment variables.
ENVIRONMENT = environ.get("ENVIRONMENT")

proc_name = "pythonmyadmin"
wsgi_app = "wsgi:app"
bind = "unix:pythonmyadmin.sock"
threads = 4
workers = 2

if ENVIRONMENT == "development" or ENVIRONMENT is None:
    reload = True
    workers = 1
    threads = 1
    bind = ["127.0.0.1:8000"]
elif ENVIRONMENT == "production":
    daemon = True
    accesslog = "/var/log/pythonmyadmin/access.log"
    errorlog = "/var/log/pythonmyadmin/error.log"
    loglevel = "trace"
    dogstatsd_tags = "env:prod,service:pythonmyadmin,language:python"
else:
    raise ValueError(f"Unknown environment provided: `{ENVIRONMENT}`. Must be `development` or `production`.")
