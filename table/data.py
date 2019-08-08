"""Fetch a database table."""
from os import environ
import pandas as pd
from sqlalchemy.types import Text, String
from sqlalchemy import create_engine


def get_table_data(table_name):
    """Fetch table from SQL database."""
    db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
    engine = create_engine(db_uri,
                           connect_args={'sslmode': 'require'},
                           echo=True)
    table_df = pd.read_sql(f'SELECT * FROM {table_name}', engine)
    return table_df


def column_dist_chart(table_df, column):
    """Aggregate column values"""
    grouped_column = table_df.groupby(column).count().sort_values(column, ascending=False)
    print('--------------------------')
    print(grouped_column)
    return grouped_column


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
