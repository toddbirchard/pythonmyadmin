"""Fetch a database table."""
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import String, Text

from config import Config

# Database connection engine
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI, connect_args=Config.SQLALCHEMY_CONNECT_ARGS
)


def get_table_data():
    """Fetch table from SQL database."""
    table_df = pd.read_sql_table(
        Config.SQLALCHEMY_DATABASE_TABLE,
        con=engine,
        index_col="id",
        parse_dates="created_at",
    )
    table_df.sort_values("created_at", ascending=False, inplace=True)
    table_df["created_at"] = table_df["created_at"].dt.strftime("%m/%d/%Y")
    return table_df


def column_dist_chart(table_df: pd.DataFrame, column):
    """Aggregate column values"""
    grouped_column = (
        table_df.groupby(column).count().sort_values(column, ascending=False)
    )
    return grouped_column


def upload_dataframe(df: pd.DataFrame):
    """Upload DataFrame database."""
    df.to_sql(
        Config.SQLALCHEMY_DATABASE_TABLE,
        engine,
        if_exists="append",
        index=True,
        dtype={"command": String(255), "response": Text},
    )
    response = f"Successfully uploaded {str(df.count)} rows."
    return response
