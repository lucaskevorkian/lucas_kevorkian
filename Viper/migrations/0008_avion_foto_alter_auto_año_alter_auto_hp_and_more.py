# Generated by Django 5.1.2 on 2024-10-26 15:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Viper', '0007_auto_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='avion',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='aviones'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='año',
            field=models.IntegerField(default=2024, error_messages={'invalid': 'El año no puede ser negativo.'}, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='auto',
            name='hp',
            field=models.IntegerField(default=0, error_messages={'invalid': 'El año no puede ser negativo.'}, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='auto',
            name='precio',
            field=models.IntegerField(default=0, error_messages={'invalid': 'El año no puede ser negativo.'}, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
