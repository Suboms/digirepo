from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from users.forms import *
from authentication.views import *
from django.shortcuts import get_object_or_404
import os

# Create your views here.


def school(request, slug):
    user=get_object_or_404(User, slug=slug)
    if request.method == "POST":
        form = SchoolProfile(request.POST, request.FILES)
        if form.is_valid():
            schools = form.save(commit=False)
            schools.save()
            return redirect(index)
    else:
        form = SchoolProfile(
            initial={"name": request.user.school_name, "email": request.user.email}
        )
    return render(request, "school/school.html", {"form": form, "user":user})


def get_states(request, pk):
    country = Country.objects.get(name=pk)
    states = State.objects.filter(country=country).values("name")
    return JsonResponse(list(states), safe=False)
