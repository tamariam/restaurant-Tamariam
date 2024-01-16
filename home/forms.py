from django import forms
from allauth.account.forms import SignupForm

'''
This is a custom signup form that extends the base SignupForm.
It adds fields for first name, last name, and modifies the email field.
'''


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=30, label='Email', required=True)

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
