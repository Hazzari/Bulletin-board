from django.contrib import admin

from .models import AdvUser


@admin.register(AdvUser)
class ProfileAdmin(admin.ModelAdmin):
    pass
