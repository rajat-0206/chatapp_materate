from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


@admin.register(room)
class roomAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    list_filter = ["members"]

@admin.register(message)
class messageAdmin(admin.ModelAdmin):
    list_display = ["group","sender","text"]
    list_filter = ["group","sender"]
