# Generated by Django 4.0.4 on 2023-04-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=30)),
                ('Product_owner_name', models.CharField(max_length=30)),
            ],
        ),
    ]
