# Generated by Django 5.1.2 on 2024-10-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Viper', '0006_auto_hp_auto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='autos'),
        ),
    ]
