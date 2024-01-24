from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

MENU_COURSES = (("mtarter", "starter"), ("main", "main"), ("dessert", "dessert"))
STATUS = ((0, "Draft"), (1, "Published"))


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default='00.00')
    avability = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(choices=MENU_COURSES, default="Main", max_length=20)
    featured_image = CloudinaryField('image', default='placeholder')
    def __str__(self):
        return self.name
