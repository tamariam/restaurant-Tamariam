from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.models import User
from .forms import CustomProfileUpdateForm
from allauth.account.views import PasswordChangeView 
from django.urls import reverse_lazy


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile_page')

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     messages.success(self.request, 'Password changed successfully.')
    #     return response
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
            # messages.add_message(request, messages.SUCCESS, 'Profile updated succesfully')
            messages.success(request, ('Account updated successfully'))
            return redirect('profile_page')
        else:
            messages.warning(request, "Profile update failed. Please correct the errors below.")
    else:
        form = CustomProfileUpdateForm(instance=user)

    return render(request, "home/update_profile.html", {'form': form})


'''delete account'''


def account_delete(request):
    if request.method == 'POST':
        if request.user == request.user:
            request.user.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('home')
        else:
            messages.error(request, 'You can only delete your own account.')
    return render(request, "home/delete_account.html")

   





