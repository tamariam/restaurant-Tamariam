from django.shortcuts import render
from .models import Menu


# Create your views here.

def menu_page(request):
    menu = Menu.objects.filter(status=1).all()
    return render(request, "menu/menu.html", {"menu" : menu})