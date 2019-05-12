"""Fetch a database table."""
from application import models
import pandas as pd


def get_data():
    """Return table from SQL database."""
    data = models.Command.query.all()
    cmd_df = pd.DataFrame([(d.command, d.response, d.type) for d in data],
                          columns=['command', 'response', 'type'])
    return cmd_df
