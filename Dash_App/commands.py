import sys
import time
from dash import Dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
from . import data
import json
from flask import current_app as app


def Add_Dash(server):
    """Plot.ly Dash view which populates the screen with loaded DataFrames."""
    external_stylesheets = ['/static/dist/css/plotly-flask-tutorial.css',
                            'https://fonts.googleapis.com/css?family=Lato::300,700',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']
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
                  <a href="/commands/"><i class="fas fa-list"></i> Commands</a>
                  <a href="/database/"><i class="fas fa-database"></i> Database</a>
                  <a href="/users/"><i class="fas fa-user-friends"></i> Users</a>
                </nav>
                <div class="layout-container">
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
    cmd_df = data.get_data()
    commands_table = create_data_table(cmd_df)

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = create_layout(commands_table)
    init_callbacks(dash_app, cmd_df)

    return dash_app.server


def create_layout(commands_table):
    """Create Dash layout for table editor."""
    return html.Div(
                    children=[commands_table,
                              html.Div(id='save', children=[html.I(className='fas fa-save'),
                                                            html.Span('Save')]),
                              html.Div(id='callback-container'),
                              html.Div(id='save-status')],
                    id='database-table-container'
                  )


def create_data_table(cmd_df):
    """Create table from Pandas DataFrame."""
    table_preview = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in cmd_df.columns],
        data=cmd_df.to_dict("rows"),
        sorting=True,
        pagination_mode="fe",
        pagination_settings={
            "displayed_pages": 1,
            "current_page": 0,
            "page_size": 50,
        },
        editable=True,
        navigation="page",
        row_deletable=True
        # filtering=True,
    )
    return table_preview


def init_callbacks(dash_app, cmd_df):
    """Dash callbacks."""
    @dash_app.callback(
        Output('save-status', 'children'),
        [Input('save', 'n_clicks'),
         Input('database-table', 'data')]
        )
    def save_table(n_clicks, table_data):
        """Save table to database."""
        updated_df = pd.DataFrame(table_data)
        sys.stdout.write(str(updated_df.info()))
        return updated_df.info()

    @dash_app.callback(
        Output('callback-container', 'children'),
        [Input('database-table', 'n_clicks'),
         Input('database-table', 'active_cell'),
         Input('database-table', 'data')]
        )
    def update_database(clicked, cell_coordinates, table_data):
        changed_cell = table_data[cell_coordinates[0]]
        return html.Span(changed_cell, className='')


'''@dash_app.callback(
    Output('callback-container', 'children'),
    [Input('database-table', 'row_update'),
        Input('database-table', 'rows')]
    )
def update_database(row_update, rows):
    return html.Div(className='row', children=[
        html.Div([
            html.Code('row_update'),
            html.Pre(json.dumps(row_update, indent=2))
        ], className='six columns'),
        html.Div([
            html.Code('rows'),
            html.Pre(json.dumps(rows, indent=2))
        ], className='six columns'),
    ])'''
