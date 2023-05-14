from django.shortcuts import render, redirect
from .forms import *
from authentication.views import *

# Create your views here.


def create_country(request):
    form = CountryCreation()
    if request.method == "POST":
        form = CountryCreation(request.POST)
        if form.is_valid():
            country_name = form.cleaned_data["name"]
            countries = country_name.split(", ")
            for country in countries:
                Country.objects.create(name=country.title())
            return redirect(index)
    else:
        form = CountryCreation()
    return render(request, "school/country.html", {"form": form})

def create_state(request):
    form = StateCreation()
    if request.method == "POST":
        form = StateCreation(request.POST)
        if form.is_valid():
            country_name = form.cleaned_data.get("country")
            state_name = form.cleaned_data.get("name")
            states = state_name.split(", ")
            for state in states:
                State.objects.create(country=country_name, name=state.title())
            return redirect(index)
    else:
        form = StateCreation()
    return render(request, "school/state.html", {"form": form})

