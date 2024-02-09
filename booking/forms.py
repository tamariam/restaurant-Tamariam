from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date", "time", "num_of_people"]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }