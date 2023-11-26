# Generated by Django 4.2.7 on 2023-11-26 11:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='Number of Owners',
            new_name='NumberofOwners',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='Price (INR)',
            new_name='Price',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='Payment Option',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='Photos (optional)',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='Vehicle Type',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='Payment',
            field=models.CharField(choices=[('Card', 'Card'), ('Net', 'Netbanking'), ('Cash', 'Cash on Delivery')], default='Card', max_length=50),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='Photos',
            field=models.ImageField(blank=True, upload_to='Photos'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='VehicleType',
            field=models.CharField(choices=[('B', 'Bike'), ('C', 'Car')], default='C', max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Contact',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('[0-9]{10}')]),
        ),
    ]
