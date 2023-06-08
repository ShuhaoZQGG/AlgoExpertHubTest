def fourNumberSum(array, targetSum):
    # Write your code here.
    map = {}
    ans = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sum = array[i] + array[j]
            if sum not in map:
                map[sum] = []
            map[sum].append((array[i], array[j]))
    for key, val in map.items():
        diff = targetSum - key
        if diff in map:
            for pairVal in val:
                i, j = pairVal
                for pairDiff in map[diff]:
                    k, v = pairDiff
                    if i not in pairDiff and j not in pairDiff and sorted([i, j, k, v]) not in ans:
                        ans.append(sorted([i,j,k,v]))
    return ans

