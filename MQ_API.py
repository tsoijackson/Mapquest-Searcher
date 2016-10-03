# project 3

import json
import urllib.parse
import urllib.request

BASE_URL = "http://open.mapquestapi.com"

API_KEY  = "FBd9aEkpUOrtk7uQHL7t24BqMOnkPdamPPPPP"

def build_url(destinations: list) -> str:
    start  = destinations[0]
    parameters  = [
        ('key', API_KEY), ('from', start),
        ]
    for place in destinations[1:]:
        parameters.append(('to', place))
    return BASE_URL + "/directions/v2/route?" + urllib.parse.urlencode(parameters)

def build_elevation_url(latlng_list: list) -> str:
    latlng = ''
    for items in latlng_list:
        lat = str(items['lat'])
        lng = str(items['lng'])
        latlng += (lat + ',')
        latlng += (lng + ',')
    print(latlng)
    parameters = [
        ('key', API_KEY),('shapeFormat', 'raw'),
        ('latLngCollection', latlng)
    ]
    return BASE_URL + "/elevation/v1/profile?" + urllib.parse.urlencode(parameters)
    
def test_response(url:str) -> bool:
    '''Test if the url can be opened'''
    try:
        response  = urllib.request.urlopen(url)
    except:
        print("MAPQUEST ERROR")
    else:
        response.close()
        return True
    
def get_response(url: str) -> 'json':
    response  = None
    try:
        response  = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding  = 'utf-8')
        return json.loads(json_text)
    except:
        print("get_response ERROR")
    finally:
        if response != None:
            response.close()

##class get_TOTALDISTANCE:
##    def get(self, json_result: 'json') -> str:
##        total_distance  = json_result['route']['distance']
##        total_distance  = str(round(total_distance))
##        return total_distance

##class get_TOTALTIME:
##    def get(self, json_result: 'json') -> str:
##        time  = json_result['route']['time']
##        time  = str(round(time/60))
##        return time
##
##class get_STEPS:
##    def get(self, json_result: 'json') -> list:
##        directions = []
##        for i in range(len(json_result['route']['legs'])):
##            for n in range(len(json_result['route']['legs'][i]['maneuvers'])):
##                directions.append(json_result['route']['legs'][i]['maneuvers'][n]['narrative'])
##        return directions
##
##class get_LATLONG:
##    def get(self, json_result: 'json') -> list:
##        latlong_list = []
##        for n in range(len(json_result['route']['locations'])):
##            latlong_list.append(json_result['route']['locations'][n]['displayLatLng'])
##        return latlong_list
##
##class get_ELEVATION:
##    def get(self, json_result: 'json') -> list:
##        elevation_list = []
##        for items in json_result['elevationProfile']:
##            elevation_list.append(items['height'])
##        return elevation_list
##
##def options(characteristics: list):
##    options  = []
##    for item in characteristics:
##        if item == 'TOTALDISTANCE':
##            options.append(print_TOTALDISTANCE())
##        elif item == 'TOTALTIME':
##            options.append(print_TOTALTIME())
##        elif item == 'STEPS':
##            options.append(print_STEPS())
##        elif item == 'LATLONG':
##            options.append(print_LATLONG())
##        elif item == 'ELEVATION':
##            options.append(print_ELEVATION())
##    return options
##            
##    
##def run_get(options: ['options'], starting_value):
##    current_value  = starting_value
##    for option in options:
##        current_value = option.get(starting_value)
##        print(current_value)
##    return current_value
        
