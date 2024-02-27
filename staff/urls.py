from django.urls import path
from .views import dashboard_page
from .views import approve_booking
from .views import reject_booking


urlpatterns = [
    path("dashboard/", dashboard_page, name='dashboard'),
    path("approve/booking/<int:pk>/", approve_booking, name='approve'),
    path("reject/booking/<int:pk>/", reject_booking, name='reject'),
]
