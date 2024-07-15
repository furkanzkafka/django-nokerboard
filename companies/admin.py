from django.contrib import admin

from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'profession', 'website', 'is_listed','is_boosted')
    list_filter = ('profession','is_listed','is_boosted')
    list_editable = ('is_listed','is_boosted')
    search_fields = ('title', 'city', 'profession', 'website', 'is_listed','is_boosted')
    list_per_page = 25

admin.site.register(Company, CompanyAdmin)