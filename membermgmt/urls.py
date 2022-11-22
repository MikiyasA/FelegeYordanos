"""felegeyordanosdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from membermgmt import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('memberDashboard/', views.mem_dashboard, name='memberDashboard'),
    path('listMembers/', views.list_members, name='listMembers'),
    path('addMembers/', views.add_members, name='addMembers'),
    path('updateMembers/<str:pk>/', views.update_member, name='updateMembers'),
    path('memberDetail/<str:pk>/', views.member_detail, name='memberDetail'),
    path('memberId/<str:pk>/', views.member_id, name='memberId'),
    path('allMemberId/', views.all_member_id, name='allMemberId'),
    path('printAllId/', views.all_to_pdf, name='printAllId'),
    path('printId/<str:pk>/', views.to_pdf, name='printId'),
    path('zemariyan/', views.list_zemari, name='zemariyan'),
    path('addFekad/', views.add_fekad, name='addFekad'),
    path('updateFekad/<str:pk>/', views.update_fekad, name='updateFekad'),
    path('listFekad/', views.list_fekad, name='listFekad'),
    path('addComment/', views.add_comment, name='addComment'),
    path('about/', views.about, name='about'),

    path('filterMember/<str:pk>/', views.list_f_members, name='filterMember'),

    #  for GodFather
    path('listGodFather/', views.list_gf, name='listGodFather'),
    path('addGodFather/', views.add_gf, name='addGodFather'),
    path('updateGodFather/<str:pk>/', views.update_gf, name='updateGodFather'),
    #  for property
    path('propertyDashboard/', views.property_dashboard, name='propertyDashboard'),
    path('listProperty/', views.list_property, name='listProperty'),
    path('addProperty/', views.add_property, name='addProperty'),
    path('updateProperty/<str:pk>/', views.update_property, name='updateProperty'),

    path('filterProperty/<str:pk>/', views.list_f_property, name='filterProperty'),

    #  for Course Student
    path('listStudent/', views.list_cstudent, name='listStudent'),
    path('addStudent/', views.add_cstudent, name='addStudent'),
    path('updateStudent/<str:pk>/', views.update_cstudent, name='updateStudent'),
    path('studentDetail/<str:pk>/', views.student_detail, name='studentDetail'),

    path('accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
