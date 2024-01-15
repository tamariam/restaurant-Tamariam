from django.urls import path
from .views import home_page
from .views import profile_page


urlpatterns = [
    path("",  home_page, name='home'),
    path("profile/", profile_page, name='profile_page')
]
