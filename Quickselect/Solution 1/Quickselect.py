def quickselect(array, k):
    # Write your code here.
    position = k - 1
    return quickSelectHelper(array, 0, len(array) - 1, position)


def quickSelectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            return -1
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        swap(pivotIdx, rightIdx, array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1


def swap(leftIdx, rightIdx, array):
    array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]