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

def check_close_to_all_locaitons(unknown_location, locations) :
    to_closest_location = 0
    closest_location = ""
    total_distance_to_all_locations = 0

    for location in locations :
        distance = abs(int(location["location"][0]) - int(unknown_location[0])) + abs(int(location["location"][1]) - int(unknown_location[1]))
        total_distance_to_all_locations += distance

    if (total_distance_to_all_locations < 10000) :
        return location
    return False

for x in range(width + 1) :
    for y in range(height + 1) :
            location = check_close_to_all_locaitons([x,y], locations)
            if (location) :
                map[x][y] = "#"
                # check the border, get the locations that extends to border
                if (x == 0 or x == width or y == 0 or y == height) :
                    location["is_infinite"] = True
            else:
                map[x][y] = "."

# not_infinite_location = list(filter(lambda location: not location["is_infinite"], locations))
# not_infinite_location.sort(key=lambda x: x["dot_count"], reverse=True)
count = 0
for x in range(width + 1) :
    for y in range(height + 1) :
        if (map[x][y] == "#") :
            count += 1
print (count)