# from django import forms
# from .models import *


# class SchoolCreationForm(forms.ModelForm):
#     class Meta:
#         model = School
#         exclude = ["created_at", "updated_at"]
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control"}),
#             "country": forms.Select(),
#             "state": forms.Select(),
#             "address": forms.TextInput(),
#             "phone": forms.TextInput(attrs={"type": "tel"}),
#             "email": forms.EmailInput(),
#             "pob": forms.EmailInput(),
#             "website": forms.TextInput(),
#             "date_established": forms.DateInput(attrs={"type": "date"}),
#         }


# class CountryCreation(forms.ModelForm):
#     class Meta:
#         model = Country
#         fields = "__all__"


# class StateCreation(forms.ModelForm):
#     class Meta:
#         model = State
#         fields = "__all__"
