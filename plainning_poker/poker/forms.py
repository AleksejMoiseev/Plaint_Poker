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