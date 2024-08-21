import dash
from dash import Dash, html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(f"{page['name']}", href=page["relative_path"]))
        for page in dash.page_registry.values()
        if page["module"] != "pages.home"  # Exclude home page
    ],
    brand="RendezView",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = dmc.MantineProvider(
    theme={"colorScheme": "light"},
    children=[
        navbar,
        dash.page_container
    ]
)

if __name__ == "__main__":
    app.run(debug=True)