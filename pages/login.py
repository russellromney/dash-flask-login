import dash
from dash import html, dcc
from auth import redirect_authenticated, unprotected

dash.register_page(__name__)


@unprotected
@redirect_authenticated("/")
def layout():
    return html.Div(
        [
            html.H2("Please log in to continue:", id="h1"),
            html.P("Try test/test"),
            dcc.Input(placeholder="Enter your username", type="text", id="uname-box"),
            dcc.Input(placeholder="Enter your password", type="password", id="pwd-box"),
            html.Button(children="Login", n_clicks=0, type="submit", id="login-button"),
            html.Div(children="", id="output-state"),
            html.Div(children="", id="login-redirect"),
        ]
    )
