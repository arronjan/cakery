import os
from django.apps import AppConfig
from django.conf import settings

class BakeryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bakery'
    # This line tells Django: "Look for the files right here in this folder"
    path = os.path.join(settings.BASE_DIR, 'bakery')