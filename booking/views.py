from django.shortcuts import render, redirect
from .models import BookingForm
from django.contrib import messages
from .models import Booking


# Create your views here.Menu.objects.filter(status=1, category='starter')

# def booking_page(request):
#     if request.method == "POST":
#         form = BookingForm(request.POST,)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Profile created succesfully')
#             return redirect('profile_page')
#         else:
#             messages.warning(request, "Booking failed. Please correct the errors below.")
#     else:
#         form = BookingForm()
#     return render(request, "booking/booking.html", {'form': form})

def booking_page(request):
    form = BookingForm()
    return render(request, "booking/booking.html", {'form': form})

