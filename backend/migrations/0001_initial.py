# Generated by Django 3.2.4 on 2021-06-15 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=256)),
                ('zip', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('private', 'Privat'), ('company', 'Company')], max_length=20)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('salutation', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('key', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('body', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('due', models.DateField()),
                ('condition', models.CharField(default='10 Tage netto', max_length=256)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.address')),
            ],
        ),
        migrations.CreateModel(
            name='InvoicePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('body', models.TextField(blank=True)),
                ('quantity', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.invoice')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contact', to='backend.contact'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.country'),
        ),
    ]
