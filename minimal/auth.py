from typing import Callable
from dash import dcc, page_registry
from flask import current_app
from flask_login import current_user


def unprotected(f: Callable) -> Callable:
    """Must be the first/outermost decorator."""
    f.is_protected = False
    return f


def protected(f: Callable) -> Callable:
    """Must be the first/outermost decorator."""
    f.is_protected = True
    return f


def _protect_layout(f: Callable) -> Callable:
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            return dcc.Location(
                id="redirect-unauthenticated-user-to-login",
                pathname=current_app.login_manager.login_view,
            )
        return f(*args, **kwargs)

    return wrapped


def redirect_authenticated(pathname: str) -> Callable:
    def wrapper(f: Callable):
        def wrapped(*args, **kwargs):
            if current_user.is_authenticated:
                return dcc.Location(
                    id="redirect-authenticated-user-to-path",
                    pathname=pathname,
                )
            return f(*args, **kwargs)

        return wrapped

    return wrapper


def protect_layouts(default: bool = True):
    for page in page_registry.values():
        if hasattr(page["layout"], "is_protected"):
            if bool(getattr(page["layout"], "is_protected")) == False:
                continue
            else:
                page["layout"] = _protect_layout(page["layout"])
        elif default == True:
            page["layout"] = _protect_layout(page["layout"])
