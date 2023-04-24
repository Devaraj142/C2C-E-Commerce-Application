# Generated by Django 4.0.4 on 2023-04-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_sales_delete_sell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=100)),
                ('phnum', models.IntegerField()),
                ('district', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('pname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('defect', models.TextField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]