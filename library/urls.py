from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib import admin

urlpatterns = [

    path('addFile/<str:pk>', views.add_file, name='addFile'),
    path('updateFile/<str:pk>/', views.update_file, name='updateFile'),

    path('folders', views.folders, name='folders'),
    path('updateFolder/<str:pk>', views.update_folder, name='updateFolder'),

    path('folders/<str:pk>', views.sub_folders, name='folders'),
    path('addFolder', views.create_folder, name='addFolder'),
    path('addSubFolder/<str:pk>/', views.add_sub_folder, name='addSubFolder'),


#    path('addContainer', views.add_container, name='/addContainer'),

#    path('shelf/<str:pk>/', views.file, name='shelf'),  # to list book
#    path('addShelf', views.add_shelf, name='addShelf'),
#    path('updateShelf/<str:pk>/', views.update_shelf, name='updateShelf'),
#    path('updateContainer/<str:pk>', views.update_container, name='updateContainer'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
