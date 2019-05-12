"""Data models."""
from . import db


class Command(db.Model):
    """Model for bot commands."""

    __tablename__ = 'acleebot'
    command = db.Column(db.String(64), unique=True, primary_key=True)
    response = db.Column(db.Text)
    type = db.Column(db.String(200))

    def __repr__(self):
        return '<Command {}>'.format(self.username)
