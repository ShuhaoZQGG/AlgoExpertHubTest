def longestSubarrayWithSum(array, targetSum):
    # Write your code here.
    result = []
    longest = 0
    ptr1, ptr2 = 0, 1
    while ptr1 < len(array) and ptr2 <= len(array):
        if sum(array[ptr1:ptr2]) == targetSum:
            length = ptr2 - ptr1 + 1
            if length >= longest:
                longest = length
                result = [ptr1, ptr2 - 1]
                ptr2 += 1
            else:
                if array[ptr1 + 1] == 0:
                    ptr2 += 1
                else:
                    ptr1 += 1
                    ptr2 = ptr1
        elif sum(array[ptr1:ptr2]) < targetSum:
            ptr2 += 1
        else:
            ptr1 += 1
            ptr2 = ptr1
    return result