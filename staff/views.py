from django.shortcuts import render,redirect
from booking.models import Booking
from django.shortcuts import get_object_or_404

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


def approve_booking(request, pk):
    # booking = get_object_or_404(Booking, id)
    booking = Booking.objects.get(id=pk)
    
    if request.method == "POST":
        booking.status = "approved"
        booking.save()
        # Redirect back to the same page
        return redirect('dashboard')  # Assuming 'dashboard' is the name of the view that renders the staff dashboard
    
    # If it's not a POST request, render the page as usual
    bookings = Booking.objects.all()
    approved = Booking.objects.filter(status='approved')
    rejected = Booking.objects.filter(status='rejected')

    context = {
        'bookings': bookings,
        'pendings': pendings,
        'approved': approved,
        'rejected': rejected,
        'booking': booking,  # Include the booking object in the context
    }
    return render(request, "staff/dashboard.html", context)
