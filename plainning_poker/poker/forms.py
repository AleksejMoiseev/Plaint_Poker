from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from poker.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        models = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = User
        fields = ('username', 'email')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'})),
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'})),
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
