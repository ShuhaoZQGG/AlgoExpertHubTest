def juiceBottling(prices):
    # Write your code here.
    cache = {0: (0, [0]), 1: (prices[1], [1])}
    for i in range(2, len(prices)):
        localMax = cache[1][0]
        localMaxList = cache[1][1]
        for j in range(i // 2, i + 1):
            print(cache)
            if i - j == 0:
                if prices[j] > localMax:
                    localMax = prices[j]
                    localMaxList = [j]
            else:
                if cache[i - j][0] + cache[j][0] > localMax:
                    localMax = cache[i - j][0] + cache[j][0]
                    localMaxList = cache[j][1] + cache[i - j][1] 
        cache[i] = (localMax, localMaxList) 
    return sorted(cache[len(prices) - 1][1])

