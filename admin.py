from django.contrib import admin
from .models import Flat


@admin.register(Flat)


class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'town',
        'address',
        'price',
        'new_building',
        'construction_year',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'town')
    search_fields = ('town', 'address')

    fieldsets = (
        (None, {
            'fields': ('town', 'address', 'price', 'owner', 'owners_phonenumber')
        }),
        (None, {
            'fields': ('construction_year', 'new_building'),
            'classes': ('collapse',)
        }),
    )
