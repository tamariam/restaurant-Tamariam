from django.urls import path
from .views import dashboard_page
from .views import approve_booking
from .views import reject_booking, search_name, search_date, today_bookings

urlpatterns = [
    path("dashboard/", dashboard_page, name='dashboard'),
    path("approve/booking/<int:pk>/", approve_booking, name='approve'),
    path("reject/booking/<int:pk>/", reject_booking, name='reject'),
    path('search/', search_name, name='search_name'),
    path('search/date/', search_date, name='search_date'),
    path('today/', today_bookings, name='today')
]
