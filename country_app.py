import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output

# instantiate the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

poverty_data = pd.read_csv("data/PovStatsData.csv")

# create app layout
app.layout = html.Div(children=[
    html.H1("Poverty And Equity Database",
            style={
                "color": "green",
                "fontSize": "40px"
            }
            ),

    html.H2("The World Bank"),

    dcc.Dropdown(
        id='country_dropdown',
        options=[{'label': country, 'value': country} for country in poverty_data['Country Name'].unique()]
    ),

    html.Br(),

    html.Div(id='report'),

    dbc.Tabs([
        dbc.Tab([
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
        ], label="Key Facts"),

        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li("Book title: Interactive Dashboards and Data Apps with Plotly and Dash"),
                html.Li([
                    "Github repo:",
                    html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                    href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')])
            ])
        ], label="Project Info")
    ])
])


@app.callback(
    Output('report', 'children'),
    Input('country_dropdown', 'value')
)
def display_country_report(country_selected: str) -> any:
    if country_selected is None:
        return ''
    else:
        filtered_df = poverty_data.loc[
            (poverty_data['Country Name'] == country_selected) &
            (poverty_data['Indicator Name'] == 'Population, total'),
            :
        ]

        population = filtered_df.loc[:, '2010'].values[0]

        return [
            html.H3(country_selected),
            f"The population of {country_selected} in 2010 was {population:,.0f}.",
            html.Br()
        ]


# run app
if __name__ == "__main__":
    app.run_server(debug=True)
