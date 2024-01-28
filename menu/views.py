from django.shortcuts import render
from .models import Menu


# Create your views here.

'''View function for rendering the menu page.'''


def menu_page(request):
    # Retrieve all menu items categorized as starters, mains, and desserts
    starters = Menu.objects.filter(status=1, category='starter')
    mains = Menu.objects.filter(status=1, category='main')
    desserts = Menu.objects.filter(status=1, category='dessert')

    # Prepare context data to pass to the template
    context = {
        'starters': starters,
        'mains': mains,
        'desserts': desserts,
    }

    # Render the menu page template with the provided context data
    return render(request, "menu/menu.html", context)
