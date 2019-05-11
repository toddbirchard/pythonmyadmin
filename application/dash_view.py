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
                    <div id="datatable-filter-container"></div>
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
    cmd_df = get_data()
    commands_table = create_data_table(cmd_df)

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = create_layout(commands_table)
    # init_callbacks(dash_app, cmd_df)

    return dash_app.server


def create_layout(commands_table):
    """Create Dash layout for table editor."""
    return html.Div(
                    children=[commands_table,
                              html.Div(id='commands-container')],
                    id='flex-container'
                  )


def get_data():
    """Return table from SQL database."""
    data = models.Command.query.all()
    cmd_df = pd.DataFrame([(d.command, d.response, d.type) for d in data],
                          columns=['command', 'response', 'type'])
    return cmd_df


def create_data_table(cmd_df):
    """Create table from Pandas DataFrame."""
    table_preview = dash_table.DataTable(
        id='commands',
        columns=[{"name": i, "id": i} for i in cmd_df.columns],
        data=cmd_df.to_dict("rows"),
        sorting=True,
        # filtering=True,
    )
    return table_preview


def init_callbacks(dash_app, cmd_df):
    @dash_app.callback(
        Output('flex-container', "children"),
        [Input('commands', "derived_virtual_data"),
         Input('commands', "derived_virtual_selected_rows")])
    def update_graph(rows, derived_virtual_selected_rows):
        # When the table is first rendered, `derived_virtual_data` and
        # `derived_virtual_selected_rows` will be `None`. This is due to an
        # idiosyncracy in Dash (unsupplied properties are always None and Dash
        # calls the dependent callbacks when the component is first rendered).
        # So, if `rows` is `None`, then the component was just rendered
        # and its value will be the same as the component's dataframe.
        # Instead of setting `None` in here, you could also set
        # `derived_virtual_data=df.to_rows('dict')` when you initialize
        # the component.
        if derived_virtual_selected_rows is None:
            derived_virtual_selected_rows = []

        if rows is None:
            dff = cmd_df
        else:
            dff = pd.DataFrame(rows)

        colors = []
        for i in range(len(dff)):
            if i in derived_virtual_selected_rows:
                colors.append("#7FDBFF")
            else:
                colors.append("#0074D9")

        return html.Div()
