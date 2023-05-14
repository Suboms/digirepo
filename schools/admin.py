from django.contrib import admin
from .models import *
from .widgets import *


class SchoolsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {"widget": PastDateField},
    }
class StateAdmin(admin.ModelAdmin):
    list_filter = ("country",)

# Register your models here.
admin.site.register(Schools, SchoolsAdmin)
admin.site.register(Country)
admin.site.register(State, StateAdmin)