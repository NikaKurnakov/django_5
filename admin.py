from django.contrib import admin
from .models import Flat


@admin.register(Flat)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    list_filter = ('town',)
    list_display = ('address', 'town', 'created_at')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('town', 'address', 'owner', 'construction_year')
        }),
        (None, {
            'fields': ('created_at',),
        }),
    )
