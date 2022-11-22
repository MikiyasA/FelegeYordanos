from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib import admin

urlpatterns = [

    path('addFile', views.add_file, name='addFile'),
    path('updateFile/<str:pk>/', views.update_file, name='updateFile'),

    path('shelf/<str:pk>/', views.file, name='shelf'),  # to list book
    path('addShelf', views.add_shelf, name='addShelf'),
    path('updateShelf/<str:pk>/', views.update_shelf, name='updateShelf'),

    path('container', views.container, name='container'),
    path('container/<str:pk>', views.shelf, name='container'),
    path('addContainer', views.add_container, name='/addContainer'),
    path('updateContainer/<str:pk>', views.update_container, name='updateContainer'),

    path('addFolder', views.add_folder, name='addFolder'),
    path('addSubFolder', views.add_sub_folder, name='addSubFolder'),
#    path('updateContainer/<str:pk>', views.update_container, name='updateContainer'),

    path('accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
