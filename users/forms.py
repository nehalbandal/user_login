from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class Registration(UserCreationForm):

    class Meta(UserCreationForm):
        model=CustomUser
        fields = ('username', 'email', 'fullname', 'age', 'address')