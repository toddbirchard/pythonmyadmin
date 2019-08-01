"""Fetch a database table."""
from os import environ
from application import models
import pandas as pd
from sqlalchemy.types import Text, String
from sqlalchemy import create_engine


def get_data():
    """Fetch table from SQL database."""
    data = models.Command.query.all()
    cmd_df = pd.DataFrame([(d.command, d.response, d.type) for d in data],
                          columns=['command', 'response', 'type'])
    return cmd_df


def upload_dataframe(commands_df):
    """Upload DataFrame to PostgreSQL database."""
    db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
    db_bot_table = environ.get('SQLALCHEMY_JIRA_TABLE')
    db_schema = environ.get('SQLALCHEMY_DB_SCHEMA')
    engine = create_engine(db_uri,
                           connect_args={'sslmode': 'require'},
                           echo=True)
    commands_df.to_sql(db_bot_table,
                       engine,
                       if_exists='append',
                       schema=db_schema,
                       index=False,
                       dtype={"command": String(100),
                              "responsetype": Text})
    success_message = 'Successfully uploaded' \
                      + str(commands_df.count) \
                      + ' rows.'
    return success_message
