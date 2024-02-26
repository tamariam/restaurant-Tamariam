from django.shortcuts import render
from booking.models import Booking

# Create your views here.


def dashboard_page(request):
    # return render('staff/dahsboard.html', {'dashboard_url': 'dashboard'})

    return render(request, "staff/dashboard.html", {'dashboard_url': 'dashboard'})

