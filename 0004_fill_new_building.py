# Generated by Django 2.2.24 on 2025-05-07 15:55

from django.db import migrations


def set_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building="Да")
    Flat.objects.filter(construction_year__lt=2015).update(new_building="Нет")


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_building),
    ]
