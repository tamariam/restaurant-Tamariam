from .models import Booking
from django import forms
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date", "time", "num_of_people"]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()})
        }