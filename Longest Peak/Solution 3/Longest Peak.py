def longestPeak(array):
    # Write your code here.
    n = len(array)
    i = 1
    ans = 0
    while (i < n):
        count = 1
        if (array[i - 1] >= array[i]):
            i += 1
            continue
        while (i < n and array[i-1] < array[i]):
            i += 1
            count += 1


        if (i >= n or array[i - 1] == array[i]):
            continue


        while (i < n and array[i-1] > array[i]):
            i += 1
            count += 1


        ans = max(ans, count)
    return ans

