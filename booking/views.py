from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Booking


# Create your views here.Menu.objects.filter(status=1, category='starter')


       
# def booking_page(request):
#     if request.user.is_authenticated:
#         form = BookingForm(data=request.POST) if request.method == "POST" else BookingForm()
#         if request.method == "POST":
#             if form.is_valid():
#                 booking = form.save(commit=False)
#                 booking.email = request.user.email
#                 booking.user = request.user
#                 booking.first_name = request.user.first_name
#                 booking.last_name = request.user.last_name
#                 booking.save()
#                 messages.add_message(request, messages.SUCCESS, 'Your booking request has been sent')
#                 return redirect('profile_page')
#             else:
#                 messages.warning(request, "Booking failed. Please correct the errors below.")
#         return render(request, "booking/booking.html", {'form': form})
#     else:
#         messages.add_message(request, messages.WARNING, 'PLEASE SIGN UP OR LIGIN FIRST TO MAKE  BOOKING')
#         return redirect('account_login')

def booking_page(request):
    if request.user.is_authenticated:
        form = BookingForm(data=request.POST) if request.method == "POST" else BookingForm()
        if request.method == "POST":
            if form.is_valid():
                booking = form.save(commit=False)
                booking.email = request.user.email
                booking.user = request.user
                booking.first_name = request.user.first_name
                booking.last_name = request.user.last_name
                booked = Booking.objects.filter(date=booking.date, time=booking.time, user=request.user)
                if booked:
                    messages.add_message(request, messages.SUCCESS, 'Your ')
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


    



