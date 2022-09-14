import phonenumbers
from django.db import migrations


def fill_owner_pure_phone_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats_to_update = []
    counter = 0
    for flat in Flat.objects.only(
            'owners_phonenumber',
            'owner_pure_phone',
    ).iterator(chunk_size=2000):
        try:
            phonenumber_obj = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            if phonenumbers.is_valid_number(phonenumber_obj):
                flat.owner_pure_phone = phonenumbers.format_number(
                    phonenumber_obj,
                    phonenumbers.PhoneNumberFormat.E164
                )
            else:
                flat.owner_pure_phone = ''
        except phonenumbers.NumberParseException:
            continue
        flats_to_update.append(flat)
        counter += 1
        if counter >= 1000:
            Flat.objects.bulk_update(flats_to_update, ['owner_pure_phone'])
            counter = 0
            flats_to_update = []
    Flat.objects.bulk_update(flats_to_update, ['owner_pure_phone'])



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20220911_2350'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone_field),
    ]
