from django.contrib import admin

from .models import Founder

class FounderAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('id', 'name')
    search_fields = ('name', 'description')
    list_per_page = 25


admin.site.register(Founder, FounderAdmin)