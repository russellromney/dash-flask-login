from dash import register_page, html
from auth import unprotected

register_page(__name__, path="/")


@unprotected
def layout():
    return html.Div(
        [
            html.H1("Welcome to the home page."),
            html.P("This page is accessible to anyone."),
        ]
    )
