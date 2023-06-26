from django.shortcuts import render
from .models import Activity

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'data/activity_list.html', {'activities': activities})

