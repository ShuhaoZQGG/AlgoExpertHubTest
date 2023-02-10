def twoNumberSum(array, targetSum):
    # Write your code here.
    sortedArr = sorted(array)
    l, h = 0, len(array) - 1
    while l < h:
        if sortedArr[l] + sortedArr[h] == targetSum:
            return [sortedArr[l],sortedArr[h]]
        elif sortedArr[l] + sortedArr[h] < targetSum:
            l += 1
        else:
            h -= 1
    return []

