from django.db import migrations


def make_owner_flat_relations(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            name=flat.owner,
            pure_phone=flat.owner_pure_phone,
            defaults={'phonenumber': flat.owners_phonenumber},
        )
        owner.flats_owned.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220912_0134'),
    ]

    operations = [
        migrations.RunPython(make_owner_flat_relations),
    ]
