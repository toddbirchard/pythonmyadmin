"""Form classes."""
from wtforms import Form, StringField, PasswordField, validators, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional


class DatabaseForm(Form):
    """Database connection Form."""

    flavor = SelectField('Database Flavor',
                         validators=[DataRequired(message=('Please select a type of database.'))])

    host = StringField('Email',
                       validators=[DataRequired(message=('Please enter a host.'))])

    port = StringField('Port',
                        validators=[DataRequired(message=('Please enter a port.')),
                                    Length(min=4, message=('Please enter a valid port.'))])

    user = StringField('Username',
                        validators=[Length(min=6, message=('Please enter a valid email address.'))])

    password = PasswordField('DB Password',
                             validators=[DataRequired(message='Please enter a password.')])

    database = StringField('Website',
                          validators=[DataRequired(message=('Please enter a database name.'))])

    schema = StringField('Schema',
                         validators=[Optional()])

    submit = SubmitField('Connect')
