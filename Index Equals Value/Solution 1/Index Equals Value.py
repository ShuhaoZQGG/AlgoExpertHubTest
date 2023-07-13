def indexEqualsValue(array):
    # Write your code here.
    l, r = 0, len(array) - 1
    index = -1
    while l <= r:
        mid = (l + r) // 2
        if mid < array[mid]:
            r = mid - 1
        elif mid > array[mid]:
            l = mid + 1
        else:
            index = mid
            r = mid - 1
    return index