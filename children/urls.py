from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib import admin

urlpatterns = [

    path('children', views.children, name='children'),
    path('listChild', views.list_child, name='listChild'),
    path('addChild', views.add_child, name='addChild'),
    path('childUpdate/<str:pk>', views.update_child, name='childUpdate'),
    path('childDetail/<str:pk>', views.child_detail, name='childDetail'),

    path('childId/<str:pk>/', views.child_id, name='childId'),
    path('allChildId/', views.all_child_id, name='allChildId'),
    path('printAllChildId/', views.all_child_to_pdf, name='printAllChildId'),
    path('printChildId/<str:pk>/', views.child_to_pdf, name='printChildId'),

    path('addCourse', views.add_course, name='addCourse'),
    path('listCourse', views.list_course, name='listCourse'),

    path('addMark', views.add_mark, name='addMark'),
    path('listMark', views.list_mark, name='listMark'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
