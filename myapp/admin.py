from django.contrib import admin
from .models import Auto

class AutoAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'transmission', 'fuel_type')
    list_filter = ('brand', 'year', 'fuel_type', 'transmission')
    search_fields = ('brand', 'model', 'color')
    ordering = ('-created_at',)

admin.site.register(Auto, AutoAdmin)
