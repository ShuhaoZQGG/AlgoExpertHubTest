def missingNumbers(nums):
    # Write your code here.
    n = len(nums) + 2
    dictionary = dict()
    for i in range(len(nums)):
        if nums[i] not in dictionary:
            dictionary[nums[i]] = True
    ans = []
    for i in range(1, n+1):
        if i not in dictionary:
            ans.append(i)
    return ans

