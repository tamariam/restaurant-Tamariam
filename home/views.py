from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home/index.html', {'home_url': 'home_page'})


def profile_page(request):
    return render(request, 'home/user_profile.html', {'profile_url': 'profile_page'})
 
