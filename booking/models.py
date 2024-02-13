from django.db import models
# from datetime import datetime, date
from django.contrib.auth.models import User
# from django.forms import ModelForm
# Create your models here.
from datetime import time


STATUS = (
    (0, "Pending"), (1, "Approved"), (2, "Rejected")
    )

PEOPLE = ((1, "1 person"),
          (2, "2 person"),
          (3, "3 person"),
          (4, "4 person"),
          (5, "5 person"),
          (6, "6 person"),
          (7, "7 person"))

TIME = (
    (time(18, 0), "18:00"),
    (time(19, 0), "19:00"), 
    (time(20, 0), "20:00"),
    (time(21, 0), "21:00"),
    (time(22, 0), "22:00"),
    (time(23, 0), "23:00")
   )


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    status = models.IntegerField(choices=STATUS, default=0)
    num_of_people = models.IntegerField(choices=PEOPLE, default=0)
    request_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField(choices=TIME, default=time(18, 0))

    def __str__(self):
        return self.first_name



