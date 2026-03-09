import os
from django.apps import AppConfig
from django.conf import settings

class BakeryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bakery'
    # This automatically finds the folder regardless of where it's hosted
    path = os.path.dirname(os.path.abspath(__file__))