"""Dash app for database table view."""
from dash import Dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from .data import get_table_data, column_dist_chart
from .layout import app_layout


def create_dash_view(server):
    """Initiate Plotly Dash view."""
    external_stylesheets = ['/static/dist/css/plotly-flask-tutorial.css',
                            'https://fonts.googleapis.com/css?family=Lato::300,700',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']
    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
                    routes_pathname_prefix='/table/commands/')

    # Override the underlying HTML template
    dash_app.index_string = app_layout

    # Get DataFrame
    table_df = get_table_data()
    commands_table = create_data_table(table_df)

    for column in table_df:
        column_dist_chart(table_df, column)

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = create_layout(commands_table)
    init_callbacks(dash_app, table_df)

    return dash_app.server


def create_layout(commands_table):
    """Create Dash layout for table editor."""
    return html.Div(id='database-table-container',
                    children=[commands_table,
                              html.Div(id='save', children=[html.I(className='fas fa-save'),
                                                            html.Span('Save')]),
                              html.Div(id='callback-container'),
                              html.Div(id='container-button-basic', children=[
                                  html.Div(id='save-status')
                              ]),
                              html.Button(
                                  'Add Row', id='editing-rows-button', n_clicks=0),
                              html.Div([
                                  dcc.Input(
                                      id='adding-rows-name',
                                      placeholder='Enter a column name...',
                                      value='',
                                      style={'padding': 10}
                                  ),
                                  html.Button('Add Column', id='adding-rows-button', n_clicks=0)
                              ], style={'height': 50}),
                              ])


def create_data_table(table_df):
    """Create table from Pandas DataFrame."""
    table_preview = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in table_df.columns],
        data=table_df.to_dict("rows"),
        sort_action="native",
        sort_mode='native',
        filter_action='native',
        page_size=9000
    )
    return table_preview


def init_callbacks(dash_app, table_df):
    """Dash callbacks."""
    @dash_app.callback(
        Output('database-table', 'data'),
        [Input('editing-rows-button', 'n_clicks')],
        [State('database-table', 'data'),
         State('database-table', 'columns')])
    def add_row(n_clicks, rows, columns):
        if n_clicks > 0:
            rows.append({c['id']: '' for c in columns})
        return rows

    @dash_app.callback(
        Output('database-table', 'columns'),
        [Input('adding-rows-button', 'n_clicks')],
        [State('adding-rows-name', 'value'),
         State('database-table', 'columns')])
    def update_columns(n_clicks, value, existing_columns):
        if n_clicks > 0:
            existing_columns.append({
                'id': value, 'name': value,
                'editable_name': True, 'deletable': True
            })
        return existing_columns

    '''@dash_app.callback(
        Output('save-status', 'children'),
        [Input('save', 'n_clicks'),
         Input('database-table', 'data')])
    def save_table(n_clicks, table_data):
        """Save table to database."""
        updated_df = pd.DataFrame(table_data)
        # print('updated_df = ', updated_df.head())
        # upload_dataframe(updated_df)
        sys.stdout.write(str(updated_df.info()))
        return updated_df'''

    '''@dash_app.callback(
        Output('callback-container', 'children'),
        [Input('database-table', 'data_timestamp'),
         Input('database-table', 'active_cell'),
         Input('database-table', 'data')])
    def update_database(time_updated, cell_coordinates, table_data):
        changed_cell = table_data[cell_coordinates[0]]
        return html.Span(changed_cell, className='')

    @dash_app.callback(
        Output('callback-container', 'children'),

        [Input('save', 'n_clicks')])
    def update_output(n_clicks, value):
        return 'The input value was "{}" and the button has been clicked {} times'.format(
            value,
            n_clicks
        )'''


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
