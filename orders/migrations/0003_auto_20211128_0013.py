# Generated by Django 3.1.4 on 2021-11-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='post_code',
            new_name='zip',
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='NE', max_length=2),
        ),
    ]