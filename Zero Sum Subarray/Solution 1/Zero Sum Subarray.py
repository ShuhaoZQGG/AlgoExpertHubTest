def zeroSumSubarray(nums):
    # Write your code here.
    windowSize = len(nums)
    while windowSize > 0:
        for i in range(len(nums)):
            if i + windowSize <= len(nums):
                if sum(nums[i:i+windowSize]) == 0:
                    return True
            else:
                break
                
        windowSize -= 1    
    return False