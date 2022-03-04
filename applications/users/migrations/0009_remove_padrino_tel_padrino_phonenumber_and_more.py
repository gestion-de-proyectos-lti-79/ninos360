# Generated by Django 4.0.2 on 2022-03-03 18:12

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_padrino_tel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='padrino',
            name='tel',
        ),
        migrations.AddField(
            model_name='padrino',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AddField(
            model_name='padrino',
            name='secondPhoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
