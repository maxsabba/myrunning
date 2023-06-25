# Generated by Django 4.2.2 on 2023-06-25 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=20)),
                ('sport_type_id', models.CharField(max_length=10)),
                ('creation_application_id', models.CharField(max_length=10)),
                ('version', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('pause', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('subjective_feeling', models.CharField(max_length=20)),
                ('dehydration_volume', models.IntegerField()),
                ('plausible', models.BooleanField()),
                ('start_time_timezone_offset', models.BigIntegerField()),
                ('end_time_timezone_offset', models.BigIntegerField()),
                ('tracking_method', models.CharField(max_length=20)),
                ('start_time', models.BigIntegerField()),
                ('end_time', models.BigIntegerField()),
                ('user_perceived_start_time', models.BigIntegerField()),
                ('user_perceived_end_time', models.BigIntegerField()),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HeartRate',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.activity')),
                ('average', models.IntegerField()),
                ('maximum', models.IntegerField()),
                ('trace_available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='InitialValues',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.activity')),
                ('distance', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('pause', models.IntegerField()),
                ('sport_type', models.JSONField()),
                ('start_time', models.BigIntegerField()),
                ('end_time', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.activity')),
                ('encoded_trace', models.TextField()),
                ('trace_available', models.BooleanField()),
                ('start_latitude', models.DecimalField(decimal_places=15, max_digits=18)),
                ('start_longitude', models.DecimalField(decimal_places=15, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.activity')),
                ('device_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.activity')),
                ('average_step_rate', models.IntegerField()),
                ('maximum_step_rate', models.IntegerField()),
                ('total_steps', models.IntegerField()),
                ('average_step_length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrackMetrics',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.activity')),
                ('distance', models.IntegerField()),
                ('average_speed', models.DecimalField(decimal_places=8, max_digits=10)),
                ('average_pace', models.DecimalField(decimal_places=16, max_digits=18)),
                ('max_speed', models.DecimalField(decimal_places=16, max_digits=18)),
                ('elevation_gain', models.IntegerField()),
                ('elevation_loss', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data.activity')),
                ('conditions', models.CharField(max_length=20)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wind_direction', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='HeartRateZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('distance', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('minimum_heart_rate', models.IntegerField()),
                ('maximum_heart_rate', models.IntegerField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.activity')),
            ],
        ),
        migrations.CreateModel(
            name='FastestSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.CharField(max_length=10)),
                ('duration', models.IntegerField()),
                ('started_at', models.BigIntegerField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.activity')),
            ],
        ),
    ]