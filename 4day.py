from pprint import pprint 

res = [0] * 60

def sort_array(el):
    return el[1:17]


def get_data():
    with open('4day.txt', "r") as f:
        fileData = f.readlines()
        fileData.sort()
        return fileData

pprint(get_data())
print(res)