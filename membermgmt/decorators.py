from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def allowed_users(*allowed_roles):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.filter(name__in=allowed_roles).exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.success(request, "እዚህ ገጽ ላይ እንዲገቡ አልተፈቀደሎትም")
                return redirect('/about')
        return wrapper_func
    return decorator
"""
@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
"""