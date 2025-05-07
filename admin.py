from django.contrib import admin
from .models import Flat


@admin.register(Flat)


class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'town', 'new_building')
    list_filter = ('new_building',)
    search_fields = ('town', 'address')
    fieldsets = (
        (None, {
            'fields': ('town', 'address', 'owner', 'owners_phonenumber', 'new_building')
        }),
    )
