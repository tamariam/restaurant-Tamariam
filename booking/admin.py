from django.contrib import admin
from .models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'status',
        'num_of_people',
        'request_date',
        'date',
        'time'
    )
    list_editable = ('status', 'num_of_people', 'date', 'time')
    list_filter = ('date', 'first_name', 'last_name')


admin.site.register(Booking, BookingAdmin)
