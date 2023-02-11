def isValidSubsequence(array, sequence):
    # Write your code here.
    arrayPtr, sequencePtr = 0, 0
    for i in range(len(array)):
        if array[arrayPtr] == sequence[sequencePtr]:
            sequencePtr += 1
            if sequencePtr == len(sequence):
                return True
        arrayPtr += 1
    if sequencePtr == len(sequence):
        return True
    return False

