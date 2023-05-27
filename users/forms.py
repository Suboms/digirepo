from django import forms
from .models import *
from schools.models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import re

User = get_user_model()


class SignUpForm(forms.ModelForm):
    """
    This is the form class that handles the registration of a new user
    """

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
            "slug",
        ]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "school_name": forms.TextInput(attrs={"class": "form-control"}),
            "school": forms.Select(attrs={"class": "form-control"}),
            "designation": forms.RadioSelect(attrs={"class": "form-check-input"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"hidden": True}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email is not None and User.objects.filter(email=email.lower()).exists():
            raise ValidationError(f"{email.lower()} already exist in database")
        return email.lower() if email else None

    def clean_school_name(self):
        name = self.cleaned_data.get("school_name")
        if name is not None and User.objects.filter(school_name=name.lower()).exists():
            raise ValidationError(f"School with the name {name.title()} already exist")
        return name.lower() if name else None

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise ValidationError("Password Mismatch")
        elif password and len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        elif password and not re.search("[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter")
        elif password and not re.search("[a-z]", password):
            raise ValidationError("Password must contain at least one lowercase letter")
        elif password and not re.search("[0-9]", password):
            raise ValidationError("Password must contain at least one digit")
        elif password and not re.search(
            "[!@#$%^&*()_+}{\":?><|\\\/,./;'[\]]", password
        ):
            raise ValidationError(
                "Password must contain at least one special character"
            )
        return cleaned_data


class SchoolProfile(forms.ModelForm):
    """
    This is a form class that handles the updating of an Higher Instution profile after an account has been created
    """

    class Meta:
        model = School
        exclude = ["created_at", "updated_at"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "readonly": True}),
            "abbr": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "state": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"type": "tel", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "pob": forms.TextInput(attrs={"class": "form-control"}),
            "date_established": forms.DateInput(attrs={"type": "date", "class":"form-control"}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
            "domain": forms.URLInput(attrs={"class": "form-control"}),
            "affiliation": forms.SelectMultiple(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "logo": forms.FileInput(attrs={"class":"form-control"}),
        }
