from django.contrib import admin

from .models import Airport, Company


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass