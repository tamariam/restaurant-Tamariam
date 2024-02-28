from django.shortcuts import render, redirect
from booking.models import Booking
from django.shortcuts import get_object_or_404
from django.contrib import messages
from simple_search import search_filter
from datetime import date
from datetime import date, timedelta

# Create your views here.


def dashboard_page(request):
    ''' View function for rendering the dashboard page for staff members.
    Retrieves all bookings from the database and categorizes them into pending,
    approved, and rejected status. Then, passes these categorized bookings as
    context variables to the dashboard template for rendering.'''
    if request.user.is_staff:
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
    else:
        messages.error(request, 'You are not authorised to view this page.')
        return redirect('home')


def approve_booking(request, pk):
    if request.user.is_staff:
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
    else:
        messages.error(request, 'You are not authorised to view this page.')
        return redirect('home')


def reject_booking(request, pk):
    if request.user.is_staff:
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
    else:
        messages.error(request, 'You are not authorised to view this page.')
        return redirect('home')


def search_name(request):
    query = request.GET.get('search_name')
    search_fields = ['first_name', 'last_name']
    f = search_filter(search_fields, query)
    filtered = Booking.objects.filter(f, status='approved')
    return render(request, 'staff/search.html', {'filtered': filtered, 'query': query})


def search_date(request):
    query = request.GET.get('search_date')
    search_fields = ['date']
    f = search_filter(search_fields, query)
    filtered = Booking.objects.filter(f, status='approved')
    return render(request, 'staff/search.html', {'filtered': filtered, 'query': query})


# def today(request):
#     today = date.today()
#     return render(request, 'staff/search.html', {'today': today})
