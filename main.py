from datetime import date, timedelta
from dash import dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from pages.home import return_home_page
from pages.organiser import return_organiser_page
from pages.attendee import return_attendee_page

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "w-50",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "25rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Keep your SIDEBAR_STYLE and CONTENT_STYLE definitions here

sidebar = html.Div(
    [
        html.H2("RendezView", className="display-4"),
        html.Hr(),
        html.P(
            "Synchronize schedules, maximize moments", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Organiser", href="/organiser", active="exact"),
                dbc.NavLink("Attendee", href="/attendee", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return return_home_page()
    elif pathname == "/organiser":
        return return_organiser_page(app)
    elif pathname == "/attendee":
        return return_attendee_page()
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    app.run(port=8888, debug=True)
