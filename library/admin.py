from django.contrib import admin
from django.apps import apps
from . models import *
# Register your models here.

models = apps.get_app_config('library').get_models()
for model in models:
    admin.site.register(model)


