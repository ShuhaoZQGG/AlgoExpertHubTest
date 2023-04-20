import math
def bestSeat(seats):
    # Write your code here.
    maxLength = -1
    index = -1
    currentLength = 0
    for i in range(len(seats)):
        if seats[i] == 0:
            currentLength = 1 if currentLength == 0 else currentLength + 1
        else:
            index = i - 1 if currentLength > maxLength else index
            maxLength = max(currentLength, maxLength)
            currentLength = 0
    return index - maxLength // 2 if maxLength != -1 else -1