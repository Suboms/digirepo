from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import logout, login
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import *
import random
import string

def generate_random_string():
    random_string = ''
    for _ in range(6):
        random_choice = random.choice(
            [random.choice(string.ascii_letters), random.choice(string.digits)])
        random_string += random_choice
    return random_string

def index(request):
    return render(request, "index.html", {})


