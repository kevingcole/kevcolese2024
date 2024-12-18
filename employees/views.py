from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Asset, Manufacturer

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def asset_list(request):
    assets = Asset.objects.select_related('manufacturer', 'assigned_to').all()
    return render(request, 'employees/asset_list.html', {'assets': assets})

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'employees/manufacturer_list.html', {'manufacturers': manufacturers})
