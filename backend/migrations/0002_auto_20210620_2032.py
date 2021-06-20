# Generated by Django 3.2.4 on 2021-06-20 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='backend.contact'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='backend.country'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='backend.address'),
        ),
        migrations.AlterField(
            model_name='invoiceposition',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceposition', to='backend.invoice'),
        ),
    ]
