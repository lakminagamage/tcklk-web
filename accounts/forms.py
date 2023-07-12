from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserDetails(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email' ,'image', 'address', 'country', 'city', 'contact_number', 'postal_code', 'social_contacts',  'about']



