from django.shortcuts import render
from .models import Menu


# Create your views here.

def menu_page(request):
    starters = Menu.objects.filter(status=1, category='starter')
    mains = Menu.objects.filter(status=1, category='main')
    desserts = Menu.objects.filter(status=1, category='dessert')   

    context = {
        'starters': starters,
        'mains': mains,
        'desserts': desserts,
     }

    return render(request, "menu/menu.html", context)
