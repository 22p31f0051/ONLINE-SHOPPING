# Generated by Django 3.2 on 2023-11-16 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productlist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 16, 15, 34, 29, 655580)),
        ),
    ]
