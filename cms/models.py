from . import db


class Command(db.Model):
    """Model for user accounts."""

    __tablename__ = 'acleebot'
    cmd = db.Column(db.String(64), unique=True, primary_key=True)
    msg = db.Column(db.Text)
    type = db.Column(db.String(200))

    def __repr__(self):
        return '<Command {}>'.format(self.username)
