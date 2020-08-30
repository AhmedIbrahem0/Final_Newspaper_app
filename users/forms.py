from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser
class Customusercreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username','email','age')
        model = CustomUser
class Customchangeform (UserChangeForm):
    class Meta (UserChangeForm.Meta):
        model = CustomUser
        fields= ('username','email','age')
        