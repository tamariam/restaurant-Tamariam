from django.shortcuts import render
from booking.models import Booking

# Create your views here.


def dashboard_page(request):
    bookings = Booking.objects.all()
    pendings = Booking.objects.filter(status='pending')
    approved = Booking.objects.filter(status='approved')
    rejected = Booking.objects.filter(status='rejected')

    context = {
        'bookings': bookings,
        'pendings': pendings,
        'approved': approved,
        'rejected': rejected,
    }

    return render(request, "staff/dashboard.html", context)

