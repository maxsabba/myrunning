from django.shortcuts import render
from .models import Activity, InitialValues
from django.db.models import F

def activity_list(request):
    #activities = Activity.objects.filter(initialvalues__activity='313a6dc2d3684c6799a2324c35a5edcd').values('duration','calories', 'start_time', 'created_at',initialvalues_activity=F('initialvalues__activity'),initialvalues_distance=F('initialvalues__distance'))
    activities = Activity.objects.values('duration','calories', 'start_time', 'created_at',initialvalues_activity=F('initialvalues__activity'),initialvalues_distance=F('initialvalues__distance'))
    #print(activities.values())
    
    #activities =Activity.objects.values('initialvalues__activity_id')
    return render(request, 'data/activity_list.html', {'activities': activities})

