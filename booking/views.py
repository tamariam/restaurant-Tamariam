from django.shortcuts import render, redirect
from .models import BookingForm
from django.contrib import messages


# Create your views here.

def booking_page(request):
    user = request.user
    if request.method == "POST":
        form = BookingForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile created succesfully')
            return redirect('profile_page')
        else:
            messages.warning(request, "Booking failed. Please correct the errors below.")
    else:
        form = BookingForm(instance=user)
    return render(request, "booking/booking.html", {'form': form})

