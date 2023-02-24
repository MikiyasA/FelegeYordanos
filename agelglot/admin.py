from django.contrib import admin
from .models import *
from django.apps import apps

# Register your models here.

"""admin.site.register(Gedam)
admin.site.register(Guzo)
admin.site.register(BookGuzo)"""

models = apps.get_app_config('agelglot').get_models()
for model in models:
    admin.site.register(model)

