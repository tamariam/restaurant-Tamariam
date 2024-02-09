from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from .models import Booking

# Create your views here.Menu.objects.filter(status=1, category='starter')


def booking_page(request):
    if request.method == "POST":
        form = BookingForm(data=request.POST,)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your booking request has been sent')
            return redirect('profile_page')
        else:
            messages.warning(request, "Booking failed. Please correct the errors below.")
    else:
        form = BookingForm()
    return render(request, "booking/booking.html", {'form': form})



