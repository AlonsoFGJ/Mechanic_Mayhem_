# Generated by Django 5.0.6 on 2024-06-26 17:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_empleado_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='imagen',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='img'),
        ),
    ]
