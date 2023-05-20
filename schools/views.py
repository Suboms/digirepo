from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from authentication.views import *
import os

# Create your views here.



def school(request):
    countries = Country.objects.all()
    if request.method == "POST":
        form = SchoolCreationForm(request.POST, request.FILES)
        if form.is_valid():
            schools=form.save(commit=False)
            if not schools.state:
                schools.state = None
            schools.save()
            return redirect(index)  # Redirect to a success page after saving
    else:
        form = SchoolCreationForm()
    return render(request, "school/school.html", {"form": form, "countries": countries})





def get_states(request, pk):
    country = Country.objects.get(name=pk)
    states = State.objects.filter(country=country).values("name")
    return JsonResponse(list(states), safe=False)
