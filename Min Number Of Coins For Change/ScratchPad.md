<pre>
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    nums = [0] + [float("inf")] * (n)
    for denom in denoms:
        for i in range(n + 1):
            if denom <= i:
                nums[i] = min(nums[i], 1 + nums[i - denom])
    return nums[n] if nums[n] !=  float("inf") else -1
</pre>