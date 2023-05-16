from django.urls import path

from . import views

urlpatterns = [
    path("countries/", views.create_country, name="countries"),
    path("state/", views.create_state, name="state"),
    path("get_states/<str:pk>/", views.get_states, name="get_states"),
    path("school/", views.school, name="school"),
]
