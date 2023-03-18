def maxSubsetSumNoAdjacent(array):
    ans = []
    def helper(n,array, value):
        length = len(array)
        if n + 2 > length - 1:
            ans.append(value)
            return value


        elif n + 3 <= length - 1:
            helper(n + 2, array, value + array[n+2])
            helper(n + 3, array, value + array[n+3])
        else:
            helper(n + 2, array, value + array[n+2])
    
        return value
    # Write your code here.
    helper(-2, array, 0)
    helper(-1, array, 0)
    return max(ans)
    





