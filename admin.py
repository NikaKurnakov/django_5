from django.contrib import admin
from .models import Flat


@admin.register(Flat)


class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'town', 'owner')
    search_fields = ['town', 'address', 'owner']
    list_filter = ('town',)