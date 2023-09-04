from dash import html, dcc, Output, Input, callback, register_page
from auth import protected

register_page(__name__)


# this is always protected, no matter the global default.
@protected
def layout():
    return html.Div(
        [
            html.H1("Page 1"),
            html.P("Welcome to Page1. This page requires the user to be logged in."),
            dcc.Input(id="page1-input", placeholder="Type here..."),
            html.Div(id="page1-content"),
        ]
    )


@callback(Output("page1-content", "children"), Input("page1-input", "value"))
def page_1_dropdown(value):
    return f"You've typed: {value or ''}"
