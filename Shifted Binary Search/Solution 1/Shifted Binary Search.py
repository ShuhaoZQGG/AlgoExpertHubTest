def shiftedBinarySearch(array, target):
    # Write your code here.
    pivot = findPivot(array)
    if pivot:
        if target < array[0]:
            return binarySearch(array, target, pivot + 1, len(array) - 1)
        else:
            return binarySearch(array, target, 0, pivot)
    else:
        return binarySearch(array, target, 0, len(array) - 1)        


def findPivot(array):
    for i in range(0, len(array) - 1):
        if array[i + 1] < array[i]:
            return i


def binarySearch(array, target, l, r):
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1