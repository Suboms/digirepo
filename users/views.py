from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import *
from schools.views import *
import random
import string
from django.utils.text import slugify

User = get_user_model()
# Create your views here.


def generate_random_string():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=6))


def create_user(request):
    if request.method == "POST":
        random_string = generate_random_string()
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            next_url = request.POST.get("next", "/")
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.username = user.email.lower()
            user.first_name = user.first_name.lower()
            user.last_name = user.last_name.lower()
            user.password2 = None
            user.slug = slugify(f"{user.first_name} {user.last_name} {random_string}")
            user.set_password(password)
            user.save()
            return redirect(next_url)
    else:
        form = SignUpForm()
    return render(
        request,
        "accounts/createuser.html",
        {"form": form, "next": request.GET.get("next", "/")},
    )


def create_school(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            next_url = request.POST.get("next", "/")
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.username = user.email.lower()
            user.school_name = user.school_name.lower()
            user.set_password(password)
            user.password2 = None
            user.slug = (
                slugify(f"{user.school_name.strip()}") if user.school_name else ""
            )
            user.save()
            return redirect(next_url)
    else:
        form = SignUpForm()
    return render(
        request,
        "accounts/createschool.html",
        {"form": form, "next": request.GET.get("next", "/")},
    )
