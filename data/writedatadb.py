import os
import json
import django
from pathlib import Path
import fnmatch

"""
This module will be used to write json data to db. 

"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myrunning.settings')
django.setup()

from data.models import Activity, Weather, Map, TrackMetrics, FastestSegment, HeartRate, HeartRateZone, Steps, InitialValues, Origin, Groups

def write_activity(data):
    """ 
    Create Activity entry. If reach an error due []'subjective_feeling'] missing, the db will
    update using 'except' session.
    Remeber to manage this issue!!!!!!!!!!!!!!!!!
    """
    # print(f"questo è il contenuto passato: {data}")
    activity_data = data
    # I'm writing into Activity table
    try:
        activity=Activity.objects.create(
            id=activity_data['id'],
            user_id=activity_data['user_id'],
            sport_type_id=activity_data['sport_type_id'],
            creation_application_id=activity_data['creation_application_id'],
            version=activity_data['version'],
            duration=activity_data['duration'],
            pause=activity_data['pause'],
            calories=activity_data['calories'],
            #subjective_feeling=activity_data['subjective_feeling'],
            dehydration_volume=activity_data['dehydration_volume'],
            plausible=activity_data['plausible'],
            start_time_timezone_offset=activity_data['start_time_timezone_offset'],
            end_time_timezone_offset=activity_data['end_time_timezone_offset'],
            tracking_method=activity_data['tracking_method'],
            start_time=activity_data['start_time'],
            end_time=activity_data['end_time'],
            user_perceived_start_time=activity_data['user_perceived_start_time'],
            user_perceived_end_time=activity_data['user_perceived_end_time'],
            created_at=activity_data['created_at'],
            updated_at=activity_data['updated_at']
        )
       
    except:
        activity=Activity.objects.create(
        id=activity_data['id'],
        user_id=activity_data['user_id'],
        sport_type_id=activity_data['sport_type_id'],
        creation_application_id=activity_data['creation_application_id'],
        version=activity_data['version'],
        duration=activity_data['duration'],
        pause=activity_data['pause'],
        calories=activity_data['calories'],
        subjective_feeling=activity_data['subjective_feeling'],
        dehydration_volume=activity_data['dehydration_volume'],
        plausible=activity_data['plausible'],
        start_time_timezone_offset=activity_data['start_time_timezone_offset'],
        end_time_timezone_offset=activity_data['end_time_timezone_offset'],
        tracking_method=activity_data['tracking_method'],
        start_time=activity_data['start_time'],
        end_time=activity_data['end_time'],
        user_perceived_start_time=activity_data['user_perceived_start_time'],
        user_perceived_end_time=activity_data['user_perceived_end_time'],
        created_at=activity_data['created_at'],
        updated_at=activity_data['updated_at']
        )
    return(activity)
        
    print("DB Updated!!!")

def write_weather(data, activity):
    activity_data = data
    # I'm writing into Weather table
    weather_data = data
    weather = Weather.objects.create(
        activity=activity,
        conditions=weather_data['conditions'],
        temperature=weather_data['temperature'],
        wind_speed=weather_data['wind_speed'],
        wind_direction=weather_data['wind_direction'],
        humidity=weather_data['humidity']
    )

def write_map(data, activity):
    # I'm writing into Map table
    map_data = data
    map = Map.objects.create(
        activity=activity,
        encoded_trace=map_data['encoded_trace'],
        trace_available=map_data['trace_available'],
        start_latitude=map_data['start_latitude'],
        start_longitude=map_data['start_longitude']
    )

def write_trackmetrics(data, activity):
    # I'm writin into TrackMetrics table
    track_metrics_data = data['features'][2]['attributes']
    track_metrics = TrackMetrics.objects.create(
        activity=activity,
        distance=track_metrics_data['distance'],
        average_speed=track_metrics_data['average_speed'],
        average_pace=track_metrics_data['average_pace'],
        max_speed=track_metrics_data['max_speed'],
        elevation_gain=track_metrics_data['elevation_gain'],
        elevation_loss=track_metrics_data['elevation_loss']
    )

def write_fastestsegment(data, activity):
    # I'm writing into FastestSegment table
    fastest_segment_data = data['features'][3]['attributes']['segments'][0]
    fastest_segment = FastestSegment.objects.create(
        activity=activity,
        distance=fastest_segment_data['distance'],
        duration=fastest_segment_data['duration'],
        started_at=fastest_segment_data['started_at']
    )

def write_heartrate(data, activity):
    # I'm wrintin into HeartRate table
    heart_rate_data = data['features'][4]['attributes']
    heart_rate = HeartRate.objects.create(
        activity=activity,
        average=heart_rate_data['average'],
        maximum=heart_rate_data['maximum'],
        trace_available=heart_rate_data['trace_available']
    )

def write_heartratezones(data, activity):
    # I'm writinf into HeartRateZone table
    heart_rate_zones_data = data['features'][4]['attributes']['zones']                                                        
    for zone_data in heart_rate_zones_data:
        minimum_heart_rate = zone_data.get('minimum_heart_rate')  # Get the value if present or None
        maximum_heart_rate = zone_data.get('maximum_heart_rate')  # Get the value if present or None

        # Provide default values if the keys are missing
        if minimum_heart_rate is None:
            minimum_heart_rate = 0
        if maximum_heart_rate is None:
            maximum_heart_rate = 0

        HeartRateZone.objects.create(
            activity=activity,
            name=zone_data['name'],
            distance=zone_data['distance'],
            duration=zone_data['duration'],
            minimum_heart_rate=minimum_heart_rate,
            maximum_heart_rate=maximum_heart_rate
        )

def write_steps(data, activity):
    # I'm writ into Steps table
    steps_data = data['features'][5]['attributes']
    steps = Steps.objects.create(
        activity=activity,
        average_step_rate=steps_data['average_step_rate'],
        maximum_step_rate=steps_data['maximum_step_rate'],
        total_steps=steps_data['total_steps'],
        average_step_length=steps_data['average_step_length']
    )

def write_initialvalues(data, activity):
    # I'm wrinting into InitialValues table
    initial_values_data = data['features'][6]['attributes']
    initial_values = InitialValues.objects.create(
        activity=activity,
        distance=initial_values_data['distance'],
        duration=initial_values_data['duration'],
        pause=initial_values_data['pause'],
        sport_type=initial_values_data['sport_type'],
        start_time=initial_values_data['start_time'],
        end_time=initial_values_data['end_time']
    )

def write_origin(data, activity):
    # I'm writing into Origin table
    origin_data = data['features'][7]['attributes']['device']
    origin = Origin.objects.create(
        activity=activity,
        device_name=origin_data['name'],
        vendor=origin_data['vendor'],
        os_version=origin_data['os_version']
    )

def write_gropus(data, activity):
    # I'm writing Groups table    
    origin_data = data['features'][8]['attributes']['groups']
    origin = Origin.objects.create(
        activity=activity,
        id=origin_data['id'],
        type=origin_data['type'],
    )
     