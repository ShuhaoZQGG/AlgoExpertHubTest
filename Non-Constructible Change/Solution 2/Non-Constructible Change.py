def nonConstructibleChange(coins):
    # Write your code here.
    sortedCoins = sorted(coins)
    i = 0
    sum = 0
    while i < len(sortedCoins):
        if i == len(sortedCoins) - 1:
            if sortedCoins[i] > sum + 1:
                return sum + 1
            else:
                return sortedCoins[i] + sum + 1
        sum += sortedCoins[i]


        if sortedCoins[i + 1] > sum + 1:
            return sum + 1




        i += 1


    return sum + 1

