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
    email = forms.EmailField(max_length=30, label='Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set new label for the email field
        self.fields['email'].required = True
        self.fields['email'].label = 'Email'

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return user


'''
This is a custom profileupdate form that extends the base UserChangeForm.
this form gives ability toupdating user profiles, excluding the password
field, and saving the changes to the database when necessary.
It adds fields for first name, last name, and modifies the email field.
'''


class CustomProfileUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=30, label='Username')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=30, label='Email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)
        self.fields['email'].required = True

    def save(self, commit=True):
        user = self.instance
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
