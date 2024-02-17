from django.urls import path
from .views import home_page
from .views import profile_page
from .views import update_user
from .views import account_delete
from .views import CustomPasswordChangeView


urlpatterns = [
    path("",  home_page, name='home'),
    path("profile/", profile_page, name='profile_page'),
    path("update/profile/", update_user, name='update_profile'),
    path("delete/account/", account_delete, name='account_delete_page'),
    path('accounts/change/password/', CustomPasswordChangeView.as_view(), name='account_change_password'),
]
