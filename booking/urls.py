from django.urls import path
from .views import booking_page


urlpatterns = [
    path("booking/", booking_page, name='booking'),
]
