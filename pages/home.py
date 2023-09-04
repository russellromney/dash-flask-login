from dash import register_page, html
from auth import unprotected

register_page(__name__, path="/")


@unprotected
def layout():
    return html.Div(
        [
            html.H1("Welcome to the home page."),
            html.P("This page is accessible to anyone."),
            html.P(
                "This is a Dash Pages app that uses Flask-Login in a multi-page app structure."
            ),
            html.P(
                [
                    "Check out the code at ",
                    html.A(
                        "Github: dash-flask-login",
                        href="https://github.com/russellromney/dash-flask-login",
                        target="_blank",
                        referrerPolicy="no-referrer-when-downgrade",
                    ),
                ]
            ),
            html.P(
                [
                    "Check out an example of an advanced Dash authentication flow at ",
                    html.A(
                        "Github: dash-auth-flow",
                        href="https://github.com/russellromney/dash-auth-flow",
                        target="_blank",
                        referrerPolicy="no-referrer-when-downgrade",
                    ),
                ]
            ),
        ]
    )
