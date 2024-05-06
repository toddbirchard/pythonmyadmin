"""Dash app for database table view."""

from typing import List, Optional
import json

from dash import Dash, dcc, html, Input, Output, State, callback
from dash_ag_grid import AgGrid
from flask import Flask
from pandas import DataFrame

from clients import db
from table.layout import app_layout


def create_dash_view(server: Flask) -> Flask:
    """
    Initiate Plotly Dash view.

    :param Flask server: Flask server object.

    :returns: Flask
    """
    external_stylesheets = [
        "/static/dist/css/style.css",
        "https://fonts.googleapis.com/css?family=Lato::300,400,500,700",
        "https://use.fontawesome.com/releases/v5.8.1/css/all.css",
    ]
    dash_app = Dash(
        server=server,
        external_stylesheets=external_stylesheets,
        routes_pathname_prefix="/table/commands/",
    )

    # Override the underlying HTML template
    dash_app.index_string = app_layout

    # Get DataFrame
    df = db.get_table_data()
    dash_grid = create_data_grid(df)

    for column in df:
        db.column_dist_chart(df, column)

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = create_layout(dash_grid, df)
    # init_callbacks(dash_app, df)

    return dash_app.server


def create_layout(dash_grid: AgGrid, df: DataFrame) -> html.Div:
    """
    Create Dash layout for table editor.

    :param DataTable dash_table: Plotly Dash DataTable component.
    :param DataFrame table_df: DataFrame created from SQL table.

    :returns: html.Div
    """
    return html.Div(
        id="database-table-container",
        children=[
            dcc.Clipboard(
                target_id="copied-data",
                title="copy",
                style={
                    "display": "block",
                    "fontSize": 20,
                },
            ),
            html.Div(
                id="controls",
                children=[
                    dcc.Input(id="search", type="text", placeholder="Search by command"),
                    dcc.Dropdown(
                        id="type-dropdown",
                        options=[{"label": i, "value": i} for i in df.type.unique() if i],
                        multi=True,
                        placeholder="Filter by type",
                    ),
                ],
            ),
            dash_grid,
            html.Div(id="callback-container"),
            html.Div(id="container-button-basic", children=[html.Div(id="save-status")]),
        ],
    )


def create_data_grid(df: DataFrame) -> AgGrid:
    """
    Create Plotly DataTable component from Pandas DataFrame.

    :param DataFrame df: DataFrame parsed from SQL database table.

    :returns: AgGrid
    """
    grid = AgGrid(
        id="database-table",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
        dashGridOptions={
            "enableCellTextSelection": True,
            "ensureDomOrder": True,
        },
        columnSize="sizeToFit",
    )
    return grid


'''def init_callbacks(dash_app: Dash, table_df: DataFrame):
    """
    Initialize callbacks for user interactions.

    :param dash_app: Plotly Dash application object.
    :type dash_app: Dash
    :param table_df: DataFrame created from SQL table.
    :type table_df: DataFrame
    """

    @dash_app.callback(
        Output("database-table", "data"),
        [Input("type-dropdown", "value"), Input("search", "value")],
    )
    def filter_by_type(types: Optional[List[str]], search_query: Optional[str]) -> dict:
        """
        Filter data via text search or dropdowns.

        :param Optional[List[str]] types: Category associated with each row in a SQL table.
        :param Optional[str] search_query: Category associated with each row in a SQL table.

        :returns: dict
        """
        dff = table_df

        if types is not None and bool(types):
            dff = dff.loc[table_df["type"].isin(types)]

        if search_query:
            dff = dff.loc[dff["command"].str.contains(search_query.lower().strip())]

        return dff.to_dict("records")'''


@callback(
    Output(" ", "content"),
    Input("database-table", "cellClicked"),
)
def display_cell_clicked_on(cell):
    # TODO: https://dash.plotly.com/dash-ag-grid/clipboard
    print(cell)
    cell = json.dumps(cell)
    print(cell)
    return cell
