from django.db import migrations


def fill_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_field),
    ]
