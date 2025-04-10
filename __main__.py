from dash import Dash, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Welcome to My Dash App!"),
    html.Button('Click me', id='btn'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    [Input('btn', 'n_clicks')]
)
def update_output(n_clicks):
    return f'Button clicked {n_clicks} times' if n_clicks else 'No clicks yet'

if __name__ == '__main__':
    app.run(debug=True)
