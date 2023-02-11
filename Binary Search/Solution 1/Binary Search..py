def binarySearch(array, target):
    # Write your code here.
    l, r = 0, len(array) - 1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

