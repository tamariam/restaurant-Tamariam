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
                    messages.error(request, 'We are currently fully booked for this date. Please choose another date or time.')
                elif requested_people + total_people_booked > max_capacity:
                    messages.error(request,  'Sorry, your booking request exceeds the maximum capacity for this date. Please select fewer people or choose another date or time.')
                else:
                    # Update booking details and save to database
                    booking.email = request.user.email
                    booking.user = request.user
                    booking.first_name = request.user.first_name
                    booking.last_name = request.user.last_name
                    # Check if user has already booked for the same date and time
                    booked = Booking.objects.filter(date=booking.date, time=booking.time, user=request.user)
                    if booked:
                        messages.add_message(request, messages.SUCCESS, 'You already have a booking for this date and time. Please choose a different time slot.')
                    else:
                        booking.save()
                        messages.add_message(request, messages.SUCCESS, 'Your booking request has been successfully submitted! You will receive feedback from us within the next 24 hours regarding the status of your booking.')
                        return redirect('profile_page')
            else:
                messages.warning(request, "Booking failed. Please correct the errors below.")
        return render(request, "booking/booking.html", {'form': form})
    else:
        messages.add_message(request, messages.WARNING, 'To make a booking, please sign up or log in first')
        return redirect('account_login')


def update_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'booking updated succesfully')
            return redirect('update_booking')
        else:
            message.error(request,'ups')
            
    else:
        form = BookingForm()
        return render(request, "booking/update_booking", {'form': form})


    
        