import dash
from dash import dcc
from flask_login import logout_user, current_user
from auth import unprotected

dash.register_page(__name__)


@unprotected
def layout():
    if current_user.is_authenticated:
        logout_user()
    return dcc.Location(id="logout-redirect", pathname="/login")
