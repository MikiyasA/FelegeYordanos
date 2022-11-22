from django.apps import apps
from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.


class MemberCreateAdmin(admin.ModelAdmin):
    list_display = ['idno', 'name','c_name', 'c_father_name', 'sex', 'bday','education_level', 'education', 'job', 'talent']
    form = MembersCreateForm
    search_fields = ['idno', 'name','c_name', 'c_father_name', 'sex', 'bday','education_level', 'education', 'job', 'talent']


"""admin.site.register(Members)#, MemberCreateAdmin)
admin.site.register(GodFather)
admin.site.register(Comment)
admin.site.register(Csv)
admin.site.register(Fekad)"""
models = apps.get_app_config('membermgmt').get_models()
for model in models:
    admin.site.register(model)
