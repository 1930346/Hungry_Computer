# Generated by Django 4.0.3 on 2022-04-08 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_client_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='phone',
            new_name='phone_number',
        ),
    ]