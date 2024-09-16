from django.contrib import admin

from  users.models import*


@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "is_staff",
        "email",
        "is_active",
    )