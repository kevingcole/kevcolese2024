from django.contrib import admin
from .models import Employee, Asset, Manufacturer

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'phone_number')
    search_fields = ('name', 'contact_email')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'department')

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'manufacturer', 'assigned_to', 'assigned_date')
    search_fields = ('name', 'serial_number', 'manufacturer__name')
    list_filter = ('assigned_date', 'manufacturer')
