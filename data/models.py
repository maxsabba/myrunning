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
    subjective_feeling = models.CharField(max_length=20, null=True)
    dehydration_volume = models.IntegerField(null=True)
    plausible = models.BooleanField(null=True)
    start_time_timezone_offset = models.BigIntegerField(null=True)
    end_time_timezone_offset = models.BigIntegerField(null=True)
    tracking_method = models.CharField(max_length=20, null=True)
    start_time = models.BigIntegerField(null=True)
    end_time = models.BigIntegerField(null=True)
    user_perceived_start_time = models.BigIntegerField(null=True)
    user_perceived_end_time = models.BigIntegerField(null=True)
    created_at = models.BigIntegerField(null=True)
    updated_at = models.BigIntegerField(null=True)


class Weather(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    conditions = models.CharField(max_length=20, null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)


class Map(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    encoded_trace = models.TextField(null=True)
    trace_available = models.BooleanField(null=True)
    start_latitude = models.DecimalField(max_digits=18, decimal_places=15, null=True)
    start_longitude = models.DecimalField(max_digits=18, decimal_places=15, null=True)


class TrackMetrics(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    distance = models.IntegerField(null=True)
    average_speed = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    average_pace = models.DecimalField(max_digits=18, decimal_places=16, null=True)
    max_speed = models.DecimalField(max_digits=18, decimal_places=16, null=True)
    elevation_gain = models.IntegerField(null=True)
    elevation_loss = models.IntegerField(null=True)


class FastestSegment(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    distance = models.CharField(max_length=10, null=True)
    duration = models.IntegerField(null=True)
    started_at = models.BigIntegerField(null=True)


class HeartRate(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    average = models.IntegerField(null=True)
    maximum = models.IntegerField(null=True)
    trace_available = models.BooleanField(null=True)


class HeartRateZone(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    distance = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    minimum_heart_rate = models.IntegerField(default=0, null=True)
    maximum_heart_rate = models.IntegerField(default=0,null=True)
    


class Steps(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    average_step_rate = models.IntegerField(null=True)
    maximum_step_rate = models.IntegerField(null=True)
    total_steps = models.IntegerField(null=True)
    average_step_length = models.IntegerField(null=True)


class InitialValues(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    distance = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    pause = models.IntegerField(null=True)
    sport_type = models.JSONField(null=True)
    start_time = models.BigIntegerField(null=True)
    end_time = models.BigIntegerField(null=True)


class Origin(models.Model):
    activity = models.OneToOneField(Activity, primary_key=True, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=20, null=True)
    vendor = models.CharField(max_length=20, null=True)
    os_version = models.CharField(max_length=20, null=True)

   
