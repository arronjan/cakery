import os
from django.apps import AppConfig
from django.conf import settings

class BakeryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bakery'
    # This line is the "magic" fix for your specific error:
    path = '/home/terribogard/cakery/bakery'