"""Basic tests for validating app functionality."""

from pandas import DataFrame

from clients.database import Database


def test_fetch_sql_data(db: Database):
    """Test fetching data from a table."""
    data = db.get_table_data()
    assert isinstance(data, DataFrame)
