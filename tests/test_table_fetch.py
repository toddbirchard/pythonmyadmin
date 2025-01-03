"""Basic tests for validating app functionality."""

from sqlalchemy.engine import Engine

from clients.database import Database


def test_fetch_sql_data(db: Database):
    """Test fetching data from a table."""
    db_engine = db.engine
    assert isinstance(db_engine, Engine)
