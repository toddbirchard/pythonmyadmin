'''@dash_app.callback(
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

@dash_app.callback(
    Output('save-status', 'children'),
    [Input('save', 'n_clicks'),
     Input('database-table', 'data')])
def save_table(n_clicks, table_data):
    """Save table to database."""
    updated_df = pd.DataFrame(table_data)
    # print('updated_df = ', updated_df.head())
    # upload_dataframe(updated_df)
    sys.stdout.write(str(updated_df.info()))
    return updated_df

@dash_app.callback(
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

"""@dash_app.callback(
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
])"""
