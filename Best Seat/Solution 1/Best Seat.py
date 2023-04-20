import math
def bestSeat(seats):
    # Write your code here.
    maxLength = -1
    currentLength = 0
    index = -1
    for i in range(0, len(seats)):
        if seats[i] == 0:
            currentLength = 1 if currentLength == 0 else currentLength + 1
        else:
            index = i if currentLength > maxLength else index
            maxLength = max(currentLength, maxLength)
            currentLength = 0
    return index - maxLength // 2 - 1 if maxLength != -1 else -1