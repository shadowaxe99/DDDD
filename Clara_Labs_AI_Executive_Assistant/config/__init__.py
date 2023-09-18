# Clara_Labs_AI_Executive_Assistant/config/__init__.py

# This file is used to initialize the configuration of the application.

import os

from django.apps import AppConfig


class Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config'

    def ready(self):
        # Set up environment variables
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')