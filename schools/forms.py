from django import forms
from .models import *


class SchoolCreationForm(forms.ModelForm):
    class Meta:
        model = Schools
        exclude = ["created_at", "updated_at"]



class CountryCreation(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

class StateCreation(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"