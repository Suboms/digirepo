from django.shortcuts import render
from .forms import *

# Create your views here.


def create_user(request):
    form = SignupForm()
    return render(request, "accounts/createuser.html", {"form": form})

def create_school(request):
    form = SignupForm()
    return render(request, "accounts/createschool.html", {"form": form})
