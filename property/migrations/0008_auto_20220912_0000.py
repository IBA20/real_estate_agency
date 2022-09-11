import phonenumbers
from django.db import migrations


def fill_owner_pure_phone_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        try:
            phonenumber_obj = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            if phonenumbers.is_valid_number(phonenumber_obj):
                flat.owner_pure_phone = phonenumbers.format_number(phonenumber_obj, phonenumbers.PhoneNumberFormat.E164)
            else:
                flat.owner_pure_phone = ''
            flat.save()
        except phonenumbers.NumberParseException:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20220911_2350'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone_field),
    ]
