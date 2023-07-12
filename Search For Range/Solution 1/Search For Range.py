import math
def searchForRange(array, target):
    # Write your code here.
    range = [-1, - 1]
    index1 = math.inf
    index2 = -math.inf
    l, r = 0, len(array) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == array[mid]:
            if mid <= index1:
                index1 = mid
            if mid >= index2:
                index2 = mid
            radius = 1
            while mid > 0:
                if array[mid - radius] == target:
                    mid -= radius
                    index1 = mid
                else:
                    break
            while mid < len(array) - 1:
                if array[mid + radius] == target:
                    mid += radius
                    index2 = mid
                else:
                    break   
            range[0] = index1
            range[1] = index2
            break
        elif target < array[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return range

