from pprint import pprint

with open('6day.txt', 'r') as myfile :
    locations = myfile.readlines()
width = 0
height = 0

for idx, location in enumerate(locations) :
    locations[idx] = {
        "name" : idx + 1,
        "location" : [location.replace('\n', '').split(', ')[0], location.replace('\n', '').split(', ')[1]],
        "is_infinite" : False,
        "dot_count" : 1
    }
    if int(location.replace('\n', '').split(', ')[0]) > width :
        width = int(location.replace('\n', '').split(', ')[0])
    if int(location.replace('\n', '').split(', ')[1]) > height :
        height = int(location.replace('\n', '').split(', ')[1])

map = [[0 for x in range(height + 1)] for y in range(width + 1)]

for location in locations :
    map[int(location["location"][0])][int(location["location"][1])] = location["location"]

def check_closest_locaiton(unknown_location, locations) :
    to_closest_location = 0
    closest_location = ""
    is_close_to_more_than_one_location = False
    for location in locations :
        distance = abs(int(location["location"][0]) - int(unknown_location[0])) + abs(int(location["location"][1]) - int(unknown_location[1]))
        if (to_closest_location == 0 or distance < to_closest_location):
            to_closest_location = distance
            closest_location = location
            is_close_to_more_than_one_location = False
        elif (to_closest_location == distance) :
            is_close_to_more_than_one_location = True
    if (not is_close_to_more_than_one_location) :
        return closest_location
    return False

for x in range(width + 1) :
    for y in range(height + 1) :
        if map[x][y] == 0 :
            if (check_closest_locaiton([x,y], locations)) :
                location = check_closest_locaiton([x,y], locations)
                map[x][y] = location["name"]
                location["dot_count"] += 1
                # check the border, get the locations that extends to border
                if (x == 0 or x == width or y == 0 or y == height) :
                    location["is_infinite"] = True
            else:
                map[x][y] = "."

not_infinite_location = list(filter(lambda location: not location["is_infinite"], locations))
not_infinite_location.sort(key=lambda x: x["dot_count"], reverse=True)

pprint(not_infinite_location)