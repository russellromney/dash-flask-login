"""
CREDIT: 
    This code was edited from AnnMarieW's original dash-flask-login. 
    Access the original at: https://github.com/AnnMarieW/dash-flask-login/
"""

import os
from flask import Flask
from flask_login import login_user, LoginManager, UserMixin, current_user
from dash import dcc, html, Input, Output, State, no_update, page_container, Dash, callback
from auth import protect_layouts

# Exposing the Flask Server to enable configuring it for logging in
server = Flask(__name__)
# Updating the Flask Server configuration with Secret Key to encrypt the user session cookie
server.config.update(SECRET_KEY=os.getenv("SECRET_KEY", "fancy"))

# Login manager object will be used to login / logout users
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = "/login"


class User(UserMixin):
    # User data model. It has to have at least self.id as a minimum
    def __init__(self, username):
        self.id = username


@login_manager.user_loader
def load_user(username):
    """This function loads the user by user id. Typically this looks up the user from a user database.
    We won't be registering or looking up users in this example.
    So we'll simply return a User object with the passed in username.
    """
    return User(username)


# Make the Dash app.
app = Dash(
    __name__,
    server=server,
    use_pages=True,
    suppress_callback_exceptions=True,
    update_title=None,
    title="Auth Example",
)
protect_layouts(default=True)


# Keep this out of source code repository - save in a file or a database
#  passwords should be encrypted
VALID_USERNAME_PASSWORD = {"test": "test", "hello": "world"}


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dcc.Link("Go to Home", href="/"),
        html.Br(),
        html.Div(id="navbar-div"),
        html.Div(dcc.Link("Login", href="/login"), id="auth-link"),
        html.Hr(),
        page_container,
    ]
)


@callback(
    Output("navbar-div", "children"),
    Output("auth-link", "children"),
    Input("url", "pathname"),
)
def navbar_auth_link(_):
    links = html.Div(
        [
            dcc.Link("Go to Page 1", href="/page-1"),
            html.Br(),
        ],
    )
    if current_user.is_authenticated:
        return links, dcc.Link("Logout", href="/logout")
    return "", dcc.Link("Login", href="/login")


@callback(
    Output("output-state", "children"),
    Output("login-redirect", "children"),
    Input("login-button", "n_clicks"),
    State("uname-box", "value"),
    State("pwd-box", "value"),
    prevent_initial_call=True,
)
def login_button_click(n_clicks, username, password):
    if n_clicks > 0:
        if VALID_USERNAME_PASSWORD.get(username) is None:
            return "Invalid username", no_update
        if VALID_USERNAME_PASSWORD.get(username) == password:
            login_user(User(username))
            return no_update, dcc.Location(id='redirect-login-to-home',pathname='/')
        return "Incorrect  password", no_update
    return no_update, no_update


if __name__ == "__main__":
    app.run_server(debug=True)
