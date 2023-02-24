from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('listGedam', views.list_gedam, name='listGedam'),
    path('createGedam', views.create_gedam, name='createGedam'),
    path('updateGedam/<str:pk>', views.update_gedam, name='updateGedam'),

    path('listGuzo', views.list_guzo, name='listGuzo'),
    path('createGuzo', views.create_guzo, name='createGuzo'),
    path('updateGuzo/<str:pk>', views.update_guzo, name='updateGuzo'),

    path('listBooking', views.list_booking, name='listBooking'),
    path('bookGuzo', views.book_guzo, name='bookGuzo'),
    path('bookGuzoId/<str:pk>', views.book_guzo_id, name='bookGuzoId'),
    path('updateBooking/<str:pk>', views.update_booking, name='updateBooking'),

    path('detail/<str:name>/<str:pk>', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
