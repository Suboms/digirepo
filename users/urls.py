from django.urls import path

from . import views

urlpatterns = [
    path("register/user/", views.create_user, name="create-user"),
    path("register/school/", views.create_school, name="create-school"),
]
