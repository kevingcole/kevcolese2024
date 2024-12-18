from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.department})"

class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    serial_number = models.CharField(max_length=100, unique=True)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="assets", on_delete=models.PROTECT
    )
    assigned_to = models.ForeignKey(
        Employee, related_name="assets", on_delete=models.CASCADE
    )
    assigned_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.serial_number}"
