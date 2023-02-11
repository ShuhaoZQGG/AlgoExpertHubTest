def getNthFib(n):
    # Write your code here.
    ans = [0, 1]
    if n == 1:
        return ans[0]
    if n == 2:
        return ans[1]
    while n > 2:
        ans[0] = ans[0] + ans[1]
        n -= 1
        if n <= 0:
            break
        ans[1] = ans[0] + ans[1]
        n -= 1
    return ans[abs(n % 2 - 1)]

