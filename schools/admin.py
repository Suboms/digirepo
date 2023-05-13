from django.contrib import admin
from .models import *
from .widgets import *
class SchoolsAdmin(admin.ModelAdmin):
    formfield_overrides={models.DateField:{"widget":PastDateField},}

# Register your models here.
admin.site.register(Schools, SchoolsAdmin)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
