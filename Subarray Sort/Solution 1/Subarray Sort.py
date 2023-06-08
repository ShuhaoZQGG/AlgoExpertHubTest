import math
def subarraySort(array):
    # Write your code here.
    i = 0
    maximum = -math.inf
    minimum = math.inf
    ans = [-1, -1]
    while i < len(array) - 1:
        maximum = max(maximum, array[i])
        if array[i + 1] < array[i] or array[i+1] < maximum:
            ans[1] = i + 1
            minimum = min(minimum, array[i + 1])
        i += 1


    if ans[1] == -1:
        return ans
    for i in range(len(array)):
        if array[i] <= minimum:
            ans[0] = i + 1
        else:
            break


    if ans[0] == -1:
        ans[0] += 1
    return ans