def findThreeLargestNumbers(array):
    # Write your code here.
    ans = []
    for i in range(0, 3):
        ans.insert(0, max(array))
        array.remove(max(array))
    return ans

