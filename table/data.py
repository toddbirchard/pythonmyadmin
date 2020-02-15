"""Fetch a database table."""
import pandas as pd
from sqlalchemy.types import Text, String
from sqlalchemy import create_engine
from config import Config


def get_table_data():
    """Fetch table from SQL database."""
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    table_df = pd.read_sql_table(con=engine,
                                 table_name=Config.SQLALCHEMY_DATABASE_TABLE)
    table_df.reset_index(inplace=True)
    return table_df


def column_dist_chart(table_df, column):
    """Aggregate column values"""
    grouped_column = table_df.groupby(column).count().sort_values(column, ascending=False)
    return grouped_column


def upload_dataframe(commands_df):
    """Upload DataFrame to PostgreSQL database."""
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
    commands_df.to_sql(Config.SQLALCHEMY_DATABASE_TABLE,
                       engine,
                       if_exists='append',
                       index=False,
                       dtype={"command": String(100),
                              "responsetype": Text})
    success_message = 'Successfully uploaded' \
                      + str(commands_df.count) \
                      + ' rows.'
    return success_message
