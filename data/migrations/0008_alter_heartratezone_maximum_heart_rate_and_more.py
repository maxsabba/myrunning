# Generated by Django 4.2.2 on 2023-10-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_delete_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartratezone',
            name='maximum_heart_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='heartratezone',
            name='minimum_heart_rate',
            field=models.IntegerField(null=True),
        ),
    ]