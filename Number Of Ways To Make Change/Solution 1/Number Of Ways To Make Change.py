def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ans = [1] + [0] * n
    for i in range(len(denoms)):
        for j in range(1, n+1):
            if denoms[i] <= j:
                ans[j] += ans[j-denoms[i]]
    return ans[n]