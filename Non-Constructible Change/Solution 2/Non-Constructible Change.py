def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    minimum_change = 0
    for coin in coins:
        if coin > minimum_change + 1:
            break
        minimum_change += coin
    return minimum_change + 1

