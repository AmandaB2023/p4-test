from django.contrib import admin
from .models import Horse


@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'breed', 'created_on')
