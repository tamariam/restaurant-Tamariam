from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User  

'''
This is a custom signup form that extends the base SignupForm.
It adds fields for first name, last name, and modifies the email field.
'''


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=30, label='Email', required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")
        return email
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set new label for the email field
        self.fields['email'].label = 'Email *'

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return user


class CustomProfileUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=30, label='Username')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=30, label='Email', required=True)

    class Meta:
        model = User  # Use the default User model
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the help text about raw passwords
        self.fields.pop('password', None)

    def save(self, commit=True):
        user = self.instance
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user
