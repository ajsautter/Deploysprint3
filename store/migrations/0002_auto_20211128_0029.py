# Generated by Django 3.1.4 on 2021-11-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='White', max_length=25),
        ),
        migrations.AddField(
            model_name='product',
            name='sleeve',
            field=models.CharField(default='Short-Sleeve', max_length=25),
        ),
    ]