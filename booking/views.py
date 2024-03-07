from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from . models import Booking
from django.shortcuts import get_object_or_404


# Create your views here.Menu.objects.filter(status=1, category='starter')


def booking_page(request):
    if request.user.is_authenticated:
        if not request.user.is_staff:
            # Initialize form with POST data if available, otherwise empty form
            form = BookingForm(data=request.POST) \
              if request.method == "POST" else BookingForm()
            if request.method == "POST":
                if form.is_valid():
                    # Create booking object but do not save to database yet
                    booking = form.save(commit=False)
                    # Check current bookings for the selected date
                    current_bookings = Booking.objects.filter(
                        date=booking.date, status="approved")
                    # Calculate total people already booked for the selected
                    # date
                    total_people_booked = sum(
                        booking.num_of_people for booking in current_bookings)
                    # Get number of people requested for the booking
                    requested_people = booking.num_of_people
                    # Define max capacity for bookings
                    max_capacity = 7
                    # Check if booking exceeds maximum capacity or clashes with
                    # existing bookings
                    if total_people_booked >= max_capacity:
                        messages.error(
                            request,
                            'We are currently fully booked '
                            'for this date.Please choose another date or time.'
                        )
                    elif requested_people + total_people_booked > max_capacity:
                        messages.error(
                            request,
                            'Unfortunately, your booking request exceeds the '
                            'maximum capacity for this date.Select fewer '
                            'people or choose another date or time.'
                        )
                    else:
                        # Update booking details and save to database
                        booking.email = request.user.email
                        booking.user = request.user
                        booking.first_name = request.user.first_name
                        booking.last_name = request.user.last_name
                        # Check if user has already booked for the same date
                        # and time
                        booked = Booking.objects.filter(
                            date=booking.date, time=booking.time,
                            user=request.user
                        )
                        if booked:
                            messages.add_message(
                                request, messages.ERROR,
                                'You already have a booking for this date and '
                                'time. Please choose a different time slot.'
                            )
                        else:
                            booking.save()
                            messages.add_message(
                                request,
                                messages.SUCCESS,
                                'Your booking request has been successfully '
                                'submitted!You will receive feedback from us '
                                'within the next 24 hours regarding status '
                                'of your booking.'
                            )
                            return redirect('profile_page')
                else:
                    messages.error(
                        request, "Booking failed.Correct the errors below")
            return render(request, "booking/booking.html", {'form': form})
        else:
            messages.add_message(
                request,
                messages.INFO,
                'As staff member you are not authorised to view this page')
        return redirect('home')
    else:
        messages.add_message(
            request,
            messages.INFO,
            'To make a booking, please sign up or log in first')
        return redirect('account_login')


def update_booking(request, pk):
    """
        Update a booking view:
        - Updates the booking with the provided primary key.
        - Performs additional validation to ensure the user does not:
        - Update the booking with a date or time that overlaps with existing
        'bookings.
        - Exceed the maximum capacity for the requested number of people.
        - Displays error messages if the validation fails.
        - Redirects the user to the profile page upon successful booking'
        ' update.
    """
    booking = get_object_or_404(Booking, id=pk)
    if request.method == "POST":
        edit_form = BookingForm(data=request.POST, instance=booking)
        if edit_form.is_valid():
            new_booking = edit_form.save(commit=False)
            # Check if only number of people is changed
            if (new_booking.date == booking.date and
                    new_booking.time == booking.time):
                # If date and time are the same, only update number of people
                booking.num_of_people = new_booking.num_of_people
                booking.save()
                messages.success(request, 'Booking updated successfully')
                return redirect('profile_page')
            else:
                # checks if date or time is changed
                current_bookings = Booking.objects.filter(
                    date=new_booking.date, status="approved"
                )
                total_people_booked = sum(
                    booking.num_of_people for booking in current_bookings
                )
                requested_people = new_booking.num_of_people
                max_capacity = 7
                if total_people_booked >= max_capacity:
                    messages.error(
                        request,
                        'We are currently fully booked for this date. Please '
                        'choose another date or time.'
                    )
                elif requested_people + total_people_booked > max_capacity:
                    messages.error(
                        request, 
                        'Sorry, your booking request exceeds '
                        'the maximum capacity for this date. Please  '
                        'fewer people or choose another date or time.'
                    )
                else:
                    # Update booking details and save to database
                    booking.num_of_people = new_booking.num_of_people
                    booking.email = request.user.email
                    booking.user = request.user
                    booking.first_name = request.user.first_name
                    booking.last_name = request.user.last_name
                    booking.save()
                    messages.success(request, 'Booking updated successfully')
                    return redirect('profile_page')
        else:
            messages.error(request, 'There was an error updating the booking.')
    else:
        edit_form = BookingForm(instance=booking)
    return render(
        request,
        "booking/update_booking.html",
        {'form': edit_form, 'booking': booking}
    )


def delete_booking(request, pk):
    '''
    This view is responsible for processing requests to delete a booking.
    When a user clicks "delete" on the profile page's "My Bookings" section,
    this view is invoked to delete the specified booking identified by its
    primary key (pk).'''

    booking = get_object_or_404(Booking, id=pk)
    if request.method == "POST":
        if booking.user == request.user:
            booking.delete()
            messages.success(request, 'Your Booking has been deleted.')
            return redirect('profile_page')
        else:
            messages.warning(request, "You can only delete your own bookings")

    return render(request, "booking/delete_booking.html", {'booking': booking})
