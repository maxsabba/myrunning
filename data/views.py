from django.shortcuts import render
from .models import Activity, InitialValues
from django.db.models import F
from datetime import datetime, timezone

def activity_list(request):
    
    activities = Activity.objects.values('duration','calories', 'start_time', 'created_at',initialvalues_activity=F('initialvalues__activity'),initialvalues_distance=F('initialvalues__distance'), trackmetrics_average_speed=F('trackmetrics__average_speed'))
    # print(activities)
    # Convert integer timestamps to datetime objects
    for activity in activities:
        activity['created_at'] = datetime.utcfromtimestamp(activity['created_at'] / 1000).replace(tzinfo=timezone.utc)
        activity['start_time'] = datetime.utcfromtimestamp(activity['start_time'] / 1000).replace(tzinfo=timezone.utc)
        activity['duration'] = activity['duration'] / 60000

    return render(request, 'data/activity_list.html', {'activities': activities})

