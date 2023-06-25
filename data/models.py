from django.db import models


class Activity(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.CharField(max_length=20)
    sport_type_id = models.CharField(max_length=10)
    creation_application_id = models.CharField(max_length=10)
    version = models.IntegerField()
    duration = models.IntegerField()
    pause = models.IntegerField()
    calories = models.IntegerField()
    subjective_feeling = models.CharField(max_length=20)
    dehydration_volume = models.IntegerField()
    plausible = models.BooleanField()
    start_time_timezone_offset = models.BigIntegerField()
    end_time_timezone_offset = models.BigIntegerField()
    tracking_method = models.CharField(max_length=20)
    start_time = models.BigIntegerField()
    end_time = models.BigIntegerField()
    user_perceived_start_time = models.BigIntegerField()
    user_perceived_end_time = models.BigIntegerField()
    created_at = models.BigIntegerField()
    updated_at = models.BigIntegerField()


class Weather(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    conditions = models.CharField(max_length=20)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    wind_direction = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)


class Map(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    encoded_trace = models.TextField()
    trace_available = models.BooleanField()
    start_latitude = models.DecimalField(max_digits=18, decimal_places=15)
    start_longitude = models.DecimalField(max_digits=18, decimal_places=15)


class TrackMetrics(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    distance = models.IntegerField()
    average_speed = models.DecimalField(max_digits=10, decimal_places=8)
    average_pace = models.DecimalField(max_digits=18, decimal_places=16)
    max_speed = models.DecimalField(max_digits=18, decimal_places=16)
    elevation_gain = models.IntegerField()
    elevation_loss = models.IntegerField()


class FastestSegment(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    distance = models.CharField(max_length=10)
    duration = models.IntegerField()
    started_at = models.BigIntegerField()


class HeartRate(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    average = models.IntegerField()
    maximum = models.IntegerField()
    trace_available = models.BooleanField()


class HeartRateZone(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    distance = models.IntegerField()
    duration = models.IntegerField()
    minimum_heart_rate = models.IntegerField()
    maximum_heart_rate = models.IntegerField()


class Steps(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    average_step_rate = models.IntegerField()
    maximum_step_rate = models.IntegerField()
    total_steps = models.IntegerField()
    average_step_length = models.IntegerField()


class InitialValues(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    distance = models.IntegerField()
    duration = models.IntegerField()
    pause = models.IntegerField()
    sport_type = models.JSONField()
    start_time = models.BigIntegerField()
    end_time = models.BigIntegerField()


class Origin(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=20)
   
