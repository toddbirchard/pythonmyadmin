import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine
from sqlalchemy.types import String, Text, Integer, DateTime


class Database:
    def __init__(self, uri, table, args=None):
        self.uri = uri
        self.table = table
        self.args = args

    @property
    def engine(self):
        # Database connection engine
        return create_engine(self.uri, connect_args=self.args)

    def upload_dataframe(self, df: DataFrame):
        """Upload DataFrame database."""
        df.to_sql(
            self.table,
            self.engine,
            if_exists="append",
            index=True,
            dtype={
                "id": Integer,
                "command": String(255),
                "response": Text,
                "type": String(255),
                "created_at": DateTime,
            },
        )
        response = f"Successfully uploaded {str(df.count)} rows."
        return response

    def get_table_data(self):
        """Fetch table from SQL database."""
        table_df = pd.read_sql_table(
            self.table,
            con=self.engine,
            index_col="id",
            parse_dates="created_at",
        )
        table_df.sort_values("created_at", ascending=False, inplace=True)
        table_df["created_at"] = table_df["created_at"].dt.strftime("%m/%d/%Y")
        return table_df

    @staticmethod
    def column_dist_chart(table_df: DataFrame, column):
        """Aggregate column values"""
        grouped_column = (
            table_df.groupby(column).count().sort_values(column, ascending=False)
        )
        return grouped_column
