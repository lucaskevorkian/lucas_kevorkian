# Generated by Django 5.1.2 on 2024-10-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Viper', '0005_avion'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='hp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]