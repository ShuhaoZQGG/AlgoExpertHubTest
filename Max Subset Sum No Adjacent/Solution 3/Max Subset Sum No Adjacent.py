def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    n = len(array) - 1
    return helper(n, array)
def helper(i, array):
    if not array:
        return 0
    if i == 0:
        return array[0]
    elif i == 1:
        return max(array[1], array[0])
    else:
        return max(helper(i-1, array), helper(i-2, array)+array[i])
    

