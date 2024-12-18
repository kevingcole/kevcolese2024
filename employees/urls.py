from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('assets/', views.asset_list, name='asset_list'),
    path('manufacturers/', views.manufacturer_list, name='manufacturer_list'),
]
