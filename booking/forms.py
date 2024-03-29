from .models import Booking
from django import forms
from django.utils import timezone
from datetime import timedelta


class BookingForm(forms.ModelForm):
    """
    A form for creating or updating a booking.
    This form allows users to input information such as the date, time,
    and number of people for a booking. It utilizes Django's ModelForm
    functionality to directly map fields to a Booking model."""

    class Meta:
        model = Booking
        fields = ["date", "time", "num_of_people"]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # calculate minimum date
        tomorrow = timezone.now().date() + timedelta(days=1)
        self.fields['date'].widget.attrs['min'] = tomorrow
        self.fields['date'].queryset = Booking.objects.order_by('-date')
