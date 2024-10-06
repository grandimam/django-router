from django.urls import path
from django.conf.urls import url
from django.urls import get_resolver, clear_url_caches


ROUTES = []

def route(url_pattern):
    def decorator(view):
        if isinstance(view, type):
            view = view.as_view()
        ROUTES.append(path(url_pattern, view))
        return view
    return decorator

def register_routes():
    clear_url_caches()
    get_resolver().url_patterns += ROUTES
