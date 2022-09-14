from django.db import migrations


def fill_owners_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.only(
            'owner',
            'owner_pure_phone',
            'owners_phonenumber'
    ).iterator():
        Owner.objects.get_or_create(
            name=flat.owner,
            pure_phone=flat.owner_pure_phone,
            defaults={'phonenumber': flat.owners_phonenumber},
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220912_0106'),
    ]

    operations = [
        migrations.RunPython(fill_owners_data),
    ]
