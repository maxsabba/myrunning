import os
import json
import django
from pathlib import Path
import fnmatch
import data.writedatadb as wdb

"""
This module parse folder where JSON are located. for each JSON check the structure
and call the function on module writedatadb.py
"""

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
            
            """ following block check nunber of items inside activity_data['features'] """

            feature_item = len(activity_data['features']) - 1
            feature_range = range(0, feature_item)
            for key, value in activity_data.items():
                if feature_item in feature_range:
                    type_value = data['features'][feature_item]['type']
                    feature_item -= 1
                    if type_value == 'weather':
                        """ Create weather entry """
                        weather_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_weather(weather_data, object_id)
                    elif type_value == 'map':
                        """ Create Map entry """  
                        map_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_map(map_data, object_id)
                    elif type_value == 'track_metrics':
                        """ Create TrackMetrics entry """
                        track_metrics_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_map(track_metrics_data, object_id)
                    elif type_value == 'fastest_segments':
                        """ Create FastestSegment entry """
                        fastest_segment_data = activity_data['features'][feature_item]['attributes']['segments'][0]
                        wdb.write_map(fastest_segment_data, object_id)
                    elif type_value == 'heart_rate':
                        """ Create HeartRate entry """
                        heart_rate_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_map(heart_rate_data, object_id)
                    elif type_value == 'steps':
                        """ Create Steps entry """
                        steps_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_map(steps_data, object_id)
                    elif type_value == 'initial_values':
                        """ Create InitialValues entry """
                        initial_values_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_map(steps_data, object_id)
                    elif type_value == 'origin':
                        """ Create Origin entry """
                        origin_data = activity_data['features'][feature_item]['attributes']['device']
                        wdb.write_map(origin_data, object_id)
                    elif type_value == 'groups':
                        """ Create Groups entry """
                        grop_data = activity_data['features'][feature_item]['attributes']['groups']
                        wdb.write_map(grop_data, object_id)

            """ End of block """            
 
        """  heareate HeartRateZone entries 
            heart_rate_zones_data = activity_data['features'][4]['attributes']['zones'] 
            wdb.write_map(heart_rate_zones_data, object_id)

        """

           
     