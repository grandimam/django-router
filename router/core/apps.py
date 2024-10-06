from django.apps import AppConfig
import importlib
from .router import register_routes

class YourFrameworkConfig(AppConfig):
    name = 'django-router'

    def ready(self):
        for app in self.apps.get_app_configs():
            try:
                importlib.import_module(f'{app.name}.views')
            except ModuleNotFoundError:
                pass
        register_routes()
