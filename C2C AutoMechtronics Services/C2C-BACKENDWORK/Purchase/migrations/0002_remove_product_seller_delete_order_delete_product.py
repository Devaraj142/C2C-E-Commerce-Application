# Generated by Django 4.0.4 on 2023-04-24 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
