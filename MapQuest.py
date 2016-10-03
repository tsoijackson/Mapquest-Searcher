import MQ_API, Output

def Map_Quest():
    '''Project 3'''
    Location = locations()
    Address = address(Location)
    selected_options = characteristics(number_of_characteristics())
    print(MQ_API.test_response(Address))
    Map_quest_url = MQ_API.build_url(Address)
    if MQ_API.test_response(Map_quest_url):
        json_route = MQ_API.get_response(Map_quest_url)
        latlong = Output.get_LATLONG(json_route)
        elevation_url = MQ_API.build_elevation_url(latlong)
        print(elevation_url)
        print(Map_quest_url)
        print()
        json_elevation = MQ_API.get_response(elevation_url)
        print(Output.options(selected_options))
        print()
        Output.run_print_options(Output.options(selected_options), json_route, json_elevation)
    

def locations()-> str:
    '''Ask for number of locations'''
    while True:
        try:
            ask  = int(input("How many locations do you have? "))
            if ask < 2:
                print("ERROR")
                print("You must have AT LEAST 2 locations. "
                      "A location to Start and a location to End.")
            else:
                return ask
        except:
            print("ERROR. Please input a number.")

def address(locations: int) -> list:
    addresses  = []
    for i in range(locations):
        addresses.append(input(("Please Enter Destination #") + str(i+1) + ": "))
    return addresses

def number_of_characteristics():
    '''Asks for many types of characteristics does the user want'''
    while True:
        try:
            ask = int(input("How many types of characteristics do you want? (5 MAX) "))
            if ask < 1 or ask > 5:
                print("ERROR. Choose a number between 1 to 5 please.")
            else:
                return ask
        except:
            print("ERROR. Please input a number")

def characteristics(number: int) -> list:
    '''Ask what types of characterstics does the user want'''
    options  = ['LATLONG', 'STEPS', 'TOTALTIME', 'TOTALDISTANCE', 'ELEVATION']
    desired_options = []
    print("Types of characterstics: LATLONG, STEPS, TOTALTIME, TOTALDISTANCE, ELEVATION.")
    while len(desired_options) != number:
        try:
            ask = input("Please choose a characteristic: ")
            for items in options:
                if ask.upper() == items:
                    desired_options.append(items)
            print(str(number-len(desired_options)) + " types of characteristics left.")
        except:
            print("ERROR. characteristics.")
    return desired_options




if __name__ == "__main__":
    Map_Quest()
