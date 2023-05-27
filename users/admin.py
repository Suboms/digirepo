from django.contrib import admin
from users.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "school_name",
    )


admin.site.register(User, UserAdmin)
