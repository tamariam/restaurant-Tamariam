from django.shortcuts import render, redirect
from booking.models import Booking
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.


def dashboard_page(request):
    ''' View function for rendering the dashboard page for staff members.
    Retrieves all bookings from the database and categorizes them into pending,
    approved, and rejected status. Then, passes these categorized bookings as
    context variables to the dashboard template for rendering.'''

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


def booking_action(request, pk, status):
    # booking = Booking.objects.get(id=pk)
    booking = get_object_or_404(Booking, id=pk)
    if request.method == "POST":
        booking.status = status
        booking.save()
        if booking.status =="approved":
            messages.success(request, 'Booking approved.')
        elif booking.status =="rejected":
            messages.success(request, 'Booking rejected.')
        else:
            messages.success(request, 'blabalana')
        # Redirect back to the same page
        return redirect('dashboard')
    # If it's not a POST request, render the page as usual
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
    # booking = Booking.objects.get(id=pk)
    booking = get_object_or_404(Booking, id=pk)
    if request.method == "POST":
        booking.status = "approved"
        booking.save()
        messages.success(request, 'Booking Approved.')
        # Redirect back to the same page
        return redirect('dashboard')
    # If it's not a POST request, render the page as usual
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


def reject_booking(request, pk):
    booking = get_object_or_404(Booking, id=pk)
    if request.method == "POST":
        booking.status = 'rejected'
        booking.save()
        messages.error(request, 'Booking rejected.')
        # Redirect back to the same page
        return redirect('dashboard')
    # If it's not a POST request, render the page as usual
    bookings = Booking.objects.all()
    pendings = Booking.objects.filter(status='pending')
    approved = Booking.objects.filter(status='approved')
    rejected = Booking.objects.filter(status='rejected')

    context = {
        'bookings': bookings,
        'pendings': pendings,
        'approved': approved,
        'rejected': rejected,
        'booking': booking,
    }
    return render(request, "staff/dashboard.html", context)
