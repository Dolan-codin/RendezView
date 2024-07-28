from datetime import date, timedelta
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

def return_organiser_page(app):
    layout = dbc.Container(
        dbc.Row(
            dbc.Col(
                [
                    html.H2("Create a New RendezView", className="text-center mb-4"),
                    dbc.Input(
                        placeholder='Enter a name for your RendezView...',
                        type='text',
                        value='',
                        className="mb-3"
                    ),
                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        min_date_allowed=date.today(),
                        max_date_allowed=date.today() + timedelta(days=365),
                        initial_visible_month=date.today(),
                        start_date=date.today(),
                        end_date=date.today() + timedelta(days=1),
                        className="d-flex justify-content-center"
                    )
                ],
                width={"size": 6, "offset": 3},
                className="mt-5"
            ),
            justify="center",
            align="center",
            style={"height": "100vh"}
        )
    )
    return layout