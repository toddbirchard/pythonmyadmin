"""Form classes."""

from wtforms import Form, PasswordField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class DatabaseForm(Form):
    """Database connection Form."""

    flavor = SelectField(
        "Database Flavor",
        validators=[DataRequired(message="Select a type of database.")],
        choices=["MySQL", "Postgres", "SQLLite"],
    )
    host = StringField("Email", validators=[DataRequired(message="Enter a hostname.")])
    port = StringField(
        "Port",
        validators=[
            DataRequired(message="Enter a port."),
            Length(min=4, message="Enter a valid port."),
        ],
    )
    user = StringField("Username", validators=[Length(min=6, message="Enter a valid email address.")])
    password = PasswordField("DB Password", validators=[DataRequired(message="Enter a password.")])
    database = StringField("Website", validators=[DataRequired(message="Enter a database name.")])
    schema = StringField("Schema", validators=[Optional()])
    submit = SubmitField("Connect")
