import os
import json
import django
from pathlib import Path
import fnmatch
import data.writedatadb as wdb

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myrunning.settings')
django.setup()

from data.models import Activity, Weather, Map, TrackMetrics, FastestSegment, HeartRate, HeartRateZone, Steps, InitialValues, Origin, Groups

"""recursively check a folder to open new json datafile"""
entries = Path('/Users/massimosabbadini/PythonProjects/myrunning/data/json_data')
#entries = Path('/Users/massimosabbadini/Documents/Runstatic/export-20230619-000/Sport-sessions')
for entry in entries.iterdir():
    if fnmatch.fnmatch(entry, '*.json'):
        with open(entry, 'r') as file:
            data = json.load(file)
                    
            """ Create Activity entry """
            print("Sto chiamando la funzione write_activity")
            activity_data = data
            #print(activity_data)
            object_id = wdb.write_activity(activity_data)
            
            """ Create weather entry """
            weather_data = activity_data['features'][0]['attributes']
            wdb.write_weather(weather_data, object_id)   

            """ Create Map entry """  
            map_data = activity_data['features'][1]['attributes']
            wdb.write_map(map_data, object_id)

            """ Create TrackMetrics entry """
            track_metrics_data = activity_data['features'][2]['attributes']
            wdb.write_map(track_metrics_data, object_id)

            """ Create FastestSegment entry """
            fastest_segment_data = activity_data['features'][3]['attributes']['segments'][0]
            wdb.write_map(fastest_segment_data, object_id)

            """ Create HeartRate entry """
            heart_rate_data = activity_data['features'][4]['attributes']
            wdb.write_map(heart_rate_data, object_id)

            """ reate HeartRateZone entries """
            heart_rate_zones_data = activity_data['features'][4]['attributes']['zones'] 
            wdb.write_map(heart_rate_zones_data, object_id)

            """ Create Steps entry """
            steps_data = activity_data['features'][5]['attributes']
            wdb.write_map(steps_data, object_id)

            """ Create InitialValues entry """
            initial_values_data = activity_data['features'][6]['attributes']
            wdb.write_map(steps_data, object_id)

            """ Create Origin entry """
            origin_data = activity_data['features'][7]['attributes']['device']
            wdb.write_map(origin_data, object_id)

            """ Create Groups entry """
            grop_data = activity_data['features'][8]['attributes']['groups']
            wdb.write_map(grop_data, object_id)
                         
        """ 
     
        

        # Create Groups entry
        try:
            origin_data = activity_data['features'][8]['attributes']['groups']
            origin = Origin.objects.create(
                activity=activity,
                id=origin_data['id'],
                type=origin_data['type'],
            )
        except Exception as error:
            with open("list.txt","a") as list:
                list.write(str(entry) +";" + str(error) +';' +"\n")
   
 """

       