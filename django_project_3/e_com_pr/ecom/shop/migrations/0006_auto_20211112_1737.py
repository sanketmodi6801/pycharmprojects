# Generated by Django 3.2.6 on 2021-11-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.CharField(max_length=500),
        ),
    ]
