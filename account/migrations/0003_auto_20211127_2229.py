# Generated by Django 3.1.4 on 2021-11-28 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211127_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbase',
            old_name='town_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='userbase',
            old_name='us_state',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='userbase',
            old_name='zipcode',
            new_name='zip',
        ),
    ]