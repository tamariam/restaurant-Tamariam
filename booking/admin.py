from django.contrib import admin
from .models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'status', 'num_of_people', 'request_date', 'date', 'time')

admin.site.register(Booking, BookingAdmin)

