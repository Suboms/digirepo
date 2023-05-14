from django.urls import path

from . import views

urlpatterns = [
    path("countries/", views.create_country, name="countries"),
    path("state/", views.create_state, name="state"),
]
