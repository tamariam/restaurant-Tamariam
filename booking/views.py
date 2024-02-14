from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from . models import Booking


# Create your views here.Menu.objects.filter(status=1, category='starter')


def booking_page(request):
    if request.user.is_authenticated:
        # Initialize form with POST data if available, otherwise empty form
        form = BookingForm(data=request.POST) if request.method == "POST" else BookingForm()
        if request.method == "POST":
            if form.is_valid():
                # Create booking object but do not save to database yet
                booking = form.save(commit=False)
                # Check current bookings for the selected date
                current_bookings = Booking.objects.filter(date=booking.date, status=1)
                # Calculate total people already booked for the selected date
                total_people_booked = sum(booking.num_of_people for booking in current_bookings)
                # Get number of people requested for the booking
                requested_people = booking.num_of_people
                # Define max capacity for bookings
                max_capacity = 7
                # Check if booking exceeds maximum capacity or clashes with existing bookings
                if total_people_booked >= max_capacity:
                    messages.error(request, 'OOPS')
                elif requested_people + total_people_booked > max_capacity:
                    messages.error(request,  'nonononon')
                else:
                    # Update booking details and save to database
                    booking.email = request.user.email
                    booking.user = request.user
                    booking.first_name = request.user.first_name
                    booking.last_name = request.user.last_name
                    # Check if user has already booked for the same date and time
                    booked = Booking.objects.filter(date=booking.date, time=booking.time, user=request.user)
                    if booked:
                        messages.add_message(request, messages.SUCCESS, 'You are already booked for this date and time please select another time ')
                    else:
                        booking.save()
                        messages.add_message(request, messages.SUCCESS, 'Your booking request has been sent')
                        return redirect('profile_page')
            else:
                messages.warning(request, "Booking failed. Please correct the errors below.")
        return render(request, "booking/booking.html", {'form': form})
    else:
        messages.add_message(request, messages.WARNING, 'PLEASE SIGN UP OR LOGIN FIRST TO MAKE  BOOKING')
        return redirect('account_login')

    

    



