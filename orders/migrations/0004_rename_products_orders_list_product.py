# Generated by Django 3.2 on 2023-11-16 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_productlist_orders_list_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders_list',
            old_name='products',
            new_name='product',
        ),
    ]
