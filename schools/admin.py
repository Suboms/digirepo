from django.contrib import admin
from .models import *
from .widgets import *


class SchoolAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {"widget": PastDateField},
    }


class CountryAdmin(admin.ModelAdmin):
    ordering = ("name",)
    list_display = ("name", "country_code", "capital")


class StateAdmin(admin.ModelAdmin):
    list_filter = ("country",)
    ordering = ("name",)
    list_display = ("name", "country")


# Register your models here.
admin.site.register(School, SchoolAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
