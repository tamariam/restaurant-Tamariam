from django.urls import path
from .views import booking_page, update_booking, delete_booking


urlpatterns = [
    path("booking/", booking_page, name='booking'),
    path("update/booking/<int:pk>/", update_booking, name='update_booking'),
    path("delete/booking/<int:pk>/", delete_booking, name='delete_booking')
]
 