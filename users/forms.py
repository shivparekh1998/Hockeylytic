from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# TODO: add user_type to users database
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserTypeForm(forms.ModelForm):
    CHOICES = [('CH', 'Coach'), ('PR', 'Player')]
    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ['user_type']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class UserDeleteForm(forms.ModelForm):

    class Meta:
        model = User
        fields = []
