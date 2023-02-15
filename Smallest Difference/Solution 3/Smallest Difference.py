def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    smallest, pair = float('inf'), []
    oneIdx, twoIdx = 0, 0
    while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
        numOne, numTwo = arrayOne[oneIdx], arrayTwo[twoIdx]
        current = abs(numOne - numTwo)
        if current < smallest:
            smallest = current
            pair = [numOne, numTwo]
        if numOne > numTwo:
            twoIdx += 1
        else:
            oneIdx += 1
    return pair

