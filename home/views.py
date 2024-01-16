from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomProfileUpdateForm


# Create your views here.


def home_page(request):
    return render(request, 'home/index.html', {'home_url': 'home_page'})


def profile_page(request):
    return render(request, 'home/user_profile.html', {'profile_url': 'profile_page'})
    

def update_user(request):
    user = request.user

    if request.method == 'POST':
        form = CustomProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
            'Profile updated succesfully')
    
            return redirect('profile_page')
        else:
            messages.warning(request, "Profile update failed. Please correct the errors below.")
    else:
        form = CustomProfileUpdateForm(instance=user)  

    return render(request, "home/update_profile.html", {'form': form})
