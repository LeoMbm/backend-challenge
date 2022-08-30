from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from users.models import App_User

User = App_User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username"]
