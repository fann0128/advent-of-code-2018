import string
import sys

sys.setrecursionlimit(15000)

with open('5day.txt', 'r') as myfile:
    input=myfile.read().replace('\n', '')

letters = string.ascii_lowercase[:26]

def removeLetter(letter, dest):
    return dest.replace(letter.lower(), '').replace(letter.upper(), '')

def removeDuplicate(input):
    for index in range(len(input) - 1):
        if ((input[index] != input[index + 1]) and (input[index].lower() == input[index + 1].lower())) :
            return removeDuplicate(input.replace(input[index] + input[index + 1], ''))
    return len(input)

for letter in letters:
    print( letter, removeDuplicate(removeLetter(letter, input)) )
