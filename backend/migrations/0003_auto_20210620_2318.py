# Generated by Django 3.2.4 on 2021-06-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210620_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceposition',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='invoiceposition',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
