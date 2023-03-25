def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    # Write your code here.
    n = len(array)
    ans = [0] * n
    ans[0] = array[0]
    ans[1] = max(array[0], array[1])
    for i in range(2, n):
        ans[i] = max(ans[i-1], ans[i-2]+array[i])
    return ans[-1]