"""External client cionfiguration."""

from clients.database import Database
from config import Config

db = Database(
    Config.SQLALCHEMY_DATABASE_URI,
    Config.SQLALCHEMY_DATABASE_TABLE,
    Config.SQLALCHEMY_CONNECT_ARGS,
)
