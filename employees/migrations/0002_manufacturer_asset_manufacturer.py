# Generated by Django 4.2.16 on 2024-12-18 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='manufacturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='assets', to='employees.manufacturer'),
            preserve_default=False,
        ),
    ]