from dash import Dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from flask import current_app as app
from . import models


def Add_Dash(server):
    """Plot.ly Dash view which populates the screen with loaded DataFrames."""
    external_stylesheets = ['https://hackers.nyc3.cdn.digitaloceanspaces.com/css/plotly-flask-tutorial.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    routes_pathname_prefix='/commands/')

    # Override the underlying HTML template
    dash_app.index_string = '''<!DOCTYPE html>
        <html>
            <head>
                {%metas%}
                <title>{%title%}</title>
                {%favicon%}
                {%css%}
            </head>
            <body>
                <nav>
                  <a href="/"><i class="fas fa-home"></i> Home</a>
                  <a href="/dash_view/"><i class="fas fa-chart-line"></i> Embdedded Plotly Dash</a>
                </nav>
                <div style="width:95%; margin: 100px auto;">
                {%app_entry%}
                </div>
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
        </html>'''
    # Create Dash Layout comprised of Data Tables
    dash_app.layout = html.Div(
        children=get_dataset(),
        id='flex-container'
      )
    return dash_app.server


def get_dataset():
    """Return previews of all CSVs saved in /data directory."""
    data = models.Command.query.all()
    cmds_df = pd.DataFrame([(d.cmd, d.msg, d.type) for d in data],
                          columns=['cmd', 'msg', 'type'])
    table_preview = dash_table.DataTable(
        id='commands',
        columns=[{"name": i, "id": i} for i in cmds_df.columns],
        data=cmds_df.to_dict("rows"),
        sorting=True,
    )
    return table_preview
