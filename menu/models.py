from django.db import models

# Create your models here.

MENU_COURSES = ((0, "Starter"),(1, "Main"),(2, "Dessert"))
STATUS = ((0, "Draft"), (1, "Published"))


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=5, default='00.00')
    avability = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS, defaul=0, max_length=10)
    category = models.Charfield(choices=MENU_COURSES, default=1, max_length=10)

    def __str__(self):
        return self.name
