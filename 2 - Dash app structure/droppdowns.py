"""
Concepts introduced
1. Dash core components for interactive user input
2. Id for uniquely labelling each component of the app (naming is crucial as app becomes larger and more complex)
3. Dependencies - used to specify input and output for functions
4. Callback function - wrapper for Python function that is automatically called by Dash whenever the input component's property changes
"""

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Front end

app.layout = html.Div(children=[
    dcc.Dropdown(id="color_dropdown",
                 options=[{
                     "label": color,
                     "value": color
                 }
                     for color in ["blue", "green", "yellow"]
                 ]),

    html.Br(),  # line break
    html.Div(id="color_output")
])


# Back end

# order of dependencies is important - Output must be specified before input
@app.callback(
    Output("color_output", "children"),  # arguments are (dash component, component property)
    Input("color_dropdown", "value")
)
def display_selected_color(color):
    if color is None:
        color = "nothing"
    return "You selected: " + color


if __name__ == "__main__":
    app.run_server(debug=True)
