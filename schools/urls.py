from django.urls import path

from . import views

urlpatterns = [
    path("get_states/<str:pk>/", views.get_states, name="get_states"),
    path("school/", views.school, name="school"),
]
