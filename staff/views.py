from django.shortcuts import render, redirect
from booking.models import Booking
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import date
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
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

            send_mail(
                "Tamariam Restaurant Confirmation of Approval",  # Subject
                '',
                "tamariamrestaurant@gmail.com",  # Sender's email address
                [booking.email],  # Recipient's email address(es)
                html_message=render_to_string('staff/email.html', {'booking': booking}),  # HTML content
                fail_silently=False,
            )
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
            send_mail(
                "Tamariam Restaurant Confirmation of Approval",  # Subject
                "tamariamrestaurant@gmail.com",  # Sender's email address
                [booking.email],  # Recipient's email address(es)
                html_message=render_to_string('staff/reject_email.html', {'context': 'values'}),  # HTML content
                fail_silently=False,
            )
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
    # Split the query string into first name and last name
    names = query.split()
    first_name = names[0] if names else ""
    last_name = names[1] if len(names) > 1 else ""

    # Filter bookings where either first_name or last_name matches
    filtered = Booking.objects.filter(
        Q(first_name__iexact=first_name) & Q(last_name__iexact=last_name),
        status='approved'
    )
    return render(request, 'staff/search.html', {'filtered': filtered, 'query': query})


def search_date(request):
    query = request.GET.get('search_date')
    filtered = Booking.objects.filter(date=query, status='approved')
    return render(request, 'staff/search.html', {'filtered': filtered, 'query': query})


def today_bookings(request):
    filtered = Booking.objects.filter(date=date.today(), status='approved')
    today = filtered.exists()
    return render(request, 'staff/search.html', {'filtered': filtered, 'today': today})
