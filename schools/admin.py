from django.contrib import admin
from .models import *
from .widgets import *


class CountryAdmin(admin.ModelAdmin):
    ordering = ("name",)
    list_display = ("name", "country_code", "capital")


class StateAdmin(admin.ModelAdmin):
    list_filter = ("country",)
    ordering = ("name",)
    list_display = ("name", "country")


# Register your models here.
admin.site.register(School)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
