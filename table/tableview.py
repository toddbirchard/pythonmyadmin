"""Dash app for database table view."""
from dash import Dash
from dash_table import DataTable
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas import DataFrame
from .data import get_table_data, column_dist_chart
from .layout import app_layout


def create_dash_view(server):
    """Initiate Plotly Dash view."""
    external_stylesheets = [
        '/static/dist/css/plotly-flask-tutorial.css',
        'https://fonts.googleapis.com/css?family=Lato::300,700',
        'https://use.fontawesome.com/releases/v5.8.1/css/all.css'
    ]
    dash_app = Dash(
        server=server,
        external_stylesheets=external_stylesheets,
        routes_pathname_prefix='/table/commands/'
    )

    # Override the underlying HTML template
    dash_app.index_string = app_layout

    # Get DataFrame
    table_df = get_table_data()
    datatable = create_data_table(table_df)

    for column in table_df:
        column_dist_chart(table_df, column)

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = create_layout(datatable, table_df)
    init_callbacks(dash_app, table_df)

    return dash_app.server


def create_layout(datatable: DataTable, table_df: DataFrame):
    """Create Dash layout for table editor."""
    return html.Div(
        id='database-table-container',
        children=[dcc.Dropdown(
            id='type-dropdown',
            options=[{'label': i, 'value': i} for i in table_df.type.unique() if i],
            multi=True,
            placeholder='Filter commands by type'
        ),
                  datatable,
                  html.Div(id='callback-container'),
                  html.Div(
                      id='container-button-basic',
                      children=[
                          html.Div(id='save-status')
                          ]),
            ]
        )


def create_data_table(table_df: DataFrame) -> DataTable:
    """Create table from Pandas DataFrame."""
    table = DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in table_df.columns],
        data=table_df.to_dict("rows"),
        sort_action="native",
        sort_mode='native',
        page_size=9000
    )
    return table


def init_callbacks(dash_app: Dash, table_df: DataFrame):
    """Dash callbacks."""
    @dash_app.callback(
        Output('database-table', 'data'),
        [Input('type-dropdown', 'value')])
    def filter_by_type(types):
        """Updates chart based on filtering."""
        dff = table_df

        if types is not None and bool(types):
            dff = table_df.loc[table_df['type'].isin(types)]

        return dff.to_dict('records')
