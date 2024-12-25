"""PyTest mocked fixtures."""

import pytest

from clients import Database
from config import settings


@pytest.fixture
def db() -> Database:
    """Return a valid database object."""
    return Database(
        uri=settings.SQLALCHEMY_DATABASE_URI,
        table=settings.SQLALCHEMY_DATABASE_TABLE,
        args=settings.SQLALCHEMY_CONNECT_ARGS,
    )
