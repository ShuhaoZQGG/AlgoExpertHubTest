def twoNumberSum(array, targetSum):
    # Write your code here.
    hm = {}
    for i in range(len(array)):
        if targetSum - array[i] not in hm:
            hm[array[i]] = targetSum - array[i]
        else:
            return [array[i], targetSum - array[i]]
    return []