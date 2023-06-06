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


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.username = user.email.lower() if user.email else None
            user.first_name = user.first_name.lower() if user.first_name else None
            user.last_name = user.last_name.lower() if user.last_name else None
            user.school_name = user.school_name.lower() if user.school_name else None
            if user.first_name and user.last_name:
                random_string = generate_random_string()
                slug = slugify(
                    f"{user.first_name} {user.last_name} {random_string}")
                while User.objects.filter(slug=slug).exists():
                    random_string = generate_random_string()
                    slug = slugify(
                        f"{user.first_name} {user.last_name} {random_string}")

                user.slug = slug
            elif user.school_name:
                user.slug = slugify(f"{user.school_name.strip()}")
            else:
                pass
            user.set_password(form.cleaned_data.get("password"))
            user.password2 = None
            user.save()

            next_url = request.POST.get("next", "/")
            return redirect(next_url)
    else:
        form = SignUpForm()

    return render(
        request,
        "accounts/createuser.html",
        {"form": form, "next": request.GET.get("next", "/")},
    )
