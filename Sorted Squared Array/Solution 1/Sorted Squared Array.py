def sortedSquaredArray(array):
    # Write your code here.
    output = []
    l, r = 0, len(array) - 1
    while l <= r:
        lValue = array[l] ** 2
        rValue = array[r] ** 2
        if lValue > rValue:
            output.insert(0, lValue)
            l += 1
        else:
            output.insert(0, rValue)
            r -= 1
    return output
        

