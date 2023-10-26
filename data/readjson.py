"""
This script/module parse folder where JSON are located. for each JSON check the structure
and call the function on module writedatadb.py
"""

import os
import json
import django
from pathlib import Path
import fnmatch
import data.writedatadb as wdb


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myrunning.settings')
django.setup()

# from data.models import Activity, Weather, Map, TrackMetrics, FastestSegment, HeartRate, HeartRateZone, Steps, InitialValues, Origin

"""recursively check a folder to open new json datafile"""
entries = Path('/Users/massimosabbadini/PythonProjects/myrunning/data/json_data')
#entries = Path('/Users/massimosabbadini/Documents/Runstatic/export-20230619-000/Sport-sessions')
for entry in entries.iterdir():
    if fnmatch.fnmatch(entry, '*.json'):
        with open(entry, 'r') as file:
            print(f"questo è l'ultimo file: {file}")
            data = json.load(file)
                    
            """ Create Activity entry """
            # print("Sto chiamando la funzione write_activity")
            activity_data = data
            object_id = wdb.write_activity(activity_data)
             
            """ following block check nunber of items inside activity_data['features'] """
           
            feature_item = len(activity_data['features']) - 1
            items_in_range = feature_item + 1
            feature_range = range(0, items_in_range)
            for key, value in activity_data.items():
                # print(f"questa è il valore di {key} e questo è value: {value}")
                # print(f"valore di feature_item: {feature_item} e valore di {feature_range}")
                if feature_item in feature_range:
                    type_value = data['features'][feature_item]['type']
                    #print(f"Questo è il valore di type: {type_value}")
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
                        wdb.write_trackmetrics(track_metrics_data, object_id)
                    elif type_value == 'fastest_segments':
                        """ Create FastestSegment entry """
                        fastest_segment_data = activity_data['features'][feature_item]['attributes']['segments'][0]
                        wdb.write_fastestsegment(fastest_segment_data, object_id)


                    elif type_value == 'heart_rate':
                        """ Create HeartRate entry """
                        heart_rate_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_heartrate(heart_rate_data, object_id)
                        """ Create HeartRateZone entry"""
                        hr_zones_items = len(activity_data['features'][feature_item]['attributes']['zones'])-1
                        zones_counter = 0
                        for zones_counter in range(0, hr_zones_items+1):
                            zone_items = activity_data['features'][feature_item]['attributes']['zones'][zones_counter]
                            wdb.write_heartratezones(zone_items, object_id)
                            zones_counter += 1
                        
                       

                    elif type_value == 'steps':
                        """ Create Steps entry """
                        steps_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_steps(steps_data, object_id)
                    elif type_value == 'initial_values':
                        """ Create InitialValues entry """
                        initial_values_data = activity_data['features'][feature_item]['attributes']
                        wdb.write_initialvalues(initial_values_data, object_id)
                    elif type_value == 'origin':
                        """ Create Origin entry """
                        origin_data = activity_data['features'][feature_item]['attributes']['device']
                        wdb.write_origin(origin_data, object_id)
                   
                feature_item -= 1
 
            """ End of block """            
 
        """  heareate HeartRateZone entries 
            heart_rate_zones_data = activity_data['features'][4]['attributes']['zones'] 
            wdb.write_map(heart_rate_zones_data, object_id)

        """

           
     