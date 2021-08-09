import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

# instantiate the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# create app layout
app.layout = html.Div(dbc.Col(
    children=[
    html.H1("Poverty And Equity Database",
            style={
                "color": "green",
                "fontSize": "40px"
            }
            ),
    html.H2("The World Bank"),
    html.P("Key Facts:"),
    # un-ordered list
    html.Ul([
        html.Li("Number of Economies: 170"), # list items within unordered list block
        html.Li("Temporal Coverage: 1974 - 2019"),
        html.Li("Update Frequency: Quarterly"),
        html.Li([
            "Source:",
            html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                   href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
            ])
    ])
    ],
    lg={"size": 6, "offset": 4}, md=12
 )
)

# run app
if __name__ == "__main__":
    app.run_server(debug=True)