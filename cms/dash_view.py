from dash import Dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from flask import current_app as app
from . import models


def Add_Dash(server):
    """Plot.ly Dash view which populates the screen with loaded DataFrames."""
    external_stylesheets = ['/static/dist/css/plotly-flask-tutorial.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/dist/js/includes/jquery.min.js', '/static/dist/js/main.js']
    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
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
                  <a href="/dash_view/"><i class="fas fa-list"></i> Commands</a>
                </nav>
                <div style="width:95%; margin: 100px auto;">
                    <div class="filter">
                        <span>Filter by type:</span>
                        <button id="avi-filter">avi</button>
                        <button id="basic-filter">basic</button>
                        <button id="crypto-filter">crypto</button>
                        <button id="goal-filter">goal</button>
                        <button id="random-filter">random</button>
                        <button id="etc-filter">etc</button>
                    </div>
                    {%app_entry%}
                </div>
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
        </html>'''

    # Get DataFrame
    cmd_df = get_dataset()

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = html.Div(
        children=[cmd_df, html.Div(id='datatable-filter-container')],
        id='flex-container'
      )

    return dash_app.server


def get_dataset():
    """Return table from SQL database."""
    data = models.Command.query.all()
    cmd_df = pd.DataFrame([(d.command, d.response, d.type) for d in data],
                          columns=['command', 'response', 'type'])
    # cmd_df.sort_values('type', axis=1, ascending=True)
    table_preview = dash_table.DataTable(
        id='commands',
        columns=[{"name": i, "id": i} for i in cmd_df.columns],
        data=cmd_df.to_dict("rows"),
        sorting=True,
        # filtering=True,
    )
    return table_preview


'''@dash_app.callback(
    Output('datatable-filter-container', "children"),
    [Input('datatable-filtering-fe', "data")])
def update_graph(rows):
    if rows is None:
        dff = cmd_df
    else:
        dff = pd.DataFrame(rows)

    return html.Div()'''
