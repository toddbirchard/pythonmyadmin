"""Data models."""

from flask import current_app as app

from pythonmyadmin import db


class Command(db.Model):
    """Command table."""

    __tablename__ = app.config["SQLALCHEMY_DATABASE_TABLE"]
    __table_args__ = {"extend_existing": True}

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(255), index=True, unique=True)
    response = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Command id={self.id}, name={self.command}, type={self.type}>"
