# Generated by Django 4.2.2 on 2023-07-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartratezone',
            name='minimum_heart_rate',
            field=models.IntegerField(default=0),
        ),
    ]