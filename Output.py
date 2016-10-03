# project 3

class print_TOTALDISTANCE:
    def printing(self, json_result: 'json',) -> None:
        '''Prints out total distance'''
        total_distance  = json_result['route']['distance']
        total_distance  = str(round(total_distance))
        print("Total Distance: " + total_distance + " miles")

class print_TOTALTIME:
    def printing(self, json_result: 'json') -> None:
        '''Prints out time'''
        time  = json_result['route']['time']
        time  = str(round(time/60))
        print("Total Time: " + time + " minutes")

class print_STEPS:
    def printing(self, json_result: 'json') -> None:
        '''Prints out directions'''
        print("DIRECTIONS")
        print("----------")

        directions = []
        for i in range(len(json_result['route']['legs'])):
            for n in range(len(json_result['route']['legs'][i]['maneuvers'])):
                directions.append(json_result['route']['legs'][i]['maneuvers'][n]['narrative'])
    
        for i in directions:
            print(i)

def get_LATLONG(json_result: 'json') -> list:
    latlong = []
    for n in range(len(json_result['route']['locations'])):
        latlong.append(json_result['route']['locations'][n]['displayLatLng'])
    return latlong

class print_LATLONG:
    def printing(self, json_result: 'json') -> None:
        '''Prints out both Latitudes and Longitudes'''
        print("LATLONGS")
        print("--------")
        
        latlong = get_LATLONG(json_result)
        
        for items in latlong:
            lat = items['lat']
            lng = items['lng']
            if lat > 0:
                NS = 'N'
            elif lat < 0:
                NS  = 'S'
            else:
                NS = ''

            if lng > 0:
                WE = 'E'
            elif lng < 0:
                WE  = 'W'
            else:
                WE = ''
            print("{:.2f}{} {:.2f}{}".format(abs(lat), NS, abs(lng), WE))
            
class print_ELEVATION:
    def printing(self, json_result: 'json') -> None:
        '''Prints out elevations'''
        print("ELEVATION")
        print("---------")

        elevation_list = []
        for items in json_result['elevationProfile']:
            elevation_list.append(items['height'])
        
        for elevations in elevation_list:
            print(elevations)

def options(characteristics: list):
    options  = []
    for item in characteristics:
        if item == 'TOTALDISTANCE':
            options.append(print_TOTALDISTANCE())
        elif item == 'TOTALTIME':
            options.append(print_TOTALTIME())
        elif item == 'STEPS':
            options.append(print_STEPS())
        elif item == 'LATLONG':
            options.append(print_LATLONG())
        elif item == 'ELEVATION':
            options.append(print_ELEVATION())
    return options

def run_print_options(options: ['options'], json_route, json_elevation):
    print(type(options))
    for i in options:
        print(type(i))
    for option in options:
        if type(option) == print_ELEVATION:
            option.printing(json_elevation)
            print()
        else:    
            option.printing(json_route)
            print()

def print_copyright() -> None:
    print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
