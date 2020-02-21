"""Data models."""
from . import db
from config import SQLALCHEMY_DATABASE_TABLE


class Command(db.Model):
    """Model for bot commands."""

    __tablename__ = SQLALCHEMY_DATABASE_TABLE
    __table_args__ = {'extend_existing': True}
    command = db.Column(db.String(64), unique=True)
    response = db.Column(db.Text)
    type = db.Column(db.String(200))

    def __repr__(self):
        return '<Command {}>'.format(self.username)
