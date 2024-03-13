"""
URL configuration for restaurant project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("home.urls")),
    path("menu/", include("menu.urls")),
    path("booking/", include("booking.urls")),
    path('staff/', include('staff.urls'))
]

# Set custom handler for 404 errors to redirect to 'custom_404'
# view in the 'booking' app
handler404 = 'booking.views.custom_404'
