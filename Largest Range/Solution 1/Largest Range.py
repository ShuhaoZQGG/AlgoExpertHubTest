import math
def largestRange(array):
    # Write your code here.
    maxLen = -math.inf
    map = {}
    output = []
    for el in array:
        map[el] = False


    for el in array:
        length = 1
        map[el] = True
        largerEl = el + 1
        smallerEl = el - 1
        while largerEl in map:
            if map[largerEl] == False:
                map[largerEl] = True
                length += 1
            largerEl += 1
        while smallerEl in map:
            if map[smallerEl] == False:
                map[smallerEl] = True
                length += 1
            smallerEl -= 1
        if length >= maxLen:
            maxLen = length
            output = [smallerEl + 1, largerEl - 1]
    return output