from django.contrib import admin
from .models import *
from .widgets import *


class SchoolsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {"widget": PastDateField},
    }
class CountryAdmin(admin.ModelAdmin):
    ordering = ("name",)
class StateAdmin(admin.ModelAdmin):
    list_filter = ("country",)
    ordering = ("name",)
# Register your models here.
admin.site.register(Schools, SchoolsAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)