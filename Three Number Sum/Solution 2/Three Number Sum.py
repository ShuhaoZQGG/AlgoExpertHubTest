def threeNumberSum(array, targetSum):
    # Write your code here.
    ans = []
    Set = set()
    for i in range(len(array)):
        twoSumTarget = targetSum - array[i]
        slicedArray = array[0:i] + array[i+1:len(array)]
        arr = twoNumberSum(slicedArray, twoSumTarget)
        for subArr in arr:
            subArr.append(array[i])
            if len(subArr) == 3 and tuple(sorted(subArr)) not in Set:
                Set.add(tuple(sorted(subArr)))
                ans.append(sorted(subArr))
    return sorted(sorted(sorted(ans, key=lambda x: x[2]), key=lambda x:x[1]), key=lambda x:x[0])




def twoNumberSum(array, targetSum):
    # Write your code here.
    hm = {}
    ans = []
    for i in range(len(array)):
        if targetSum - array[i] not in hm:
            hm[array[i]] = targetSum - array[i]
        else:
            ans.append([array[i], targetSum - array[i]])
    return ans