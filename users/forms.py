from django import forms
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "school_name",
            "school",
            "designation",
            "avatar",
            "password",
            "password2",
        ]
        widgets = {
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "school_name":forms.TextInput(attrs={"class":"form-control"}),
            "school":forms.Select(attrs={"class":"form-control"}),
            "designation": forms.RadioSelect(attrs={"class": "form-check-input"}),
            "password": forms.PasswordInput(attrs={"class":"form-control"}),
            "password2": forms.PasswordInput(attrs={"class":"form-control"}),
        }
