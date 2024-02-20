from django.urls import path
from .views import booking_page, update_booking


urlpatterns = [
    path("booking/", booking_page, name='booking'),
    path("update/booking/<int:booking_id>/", update_booking, name='update_booking')
]
