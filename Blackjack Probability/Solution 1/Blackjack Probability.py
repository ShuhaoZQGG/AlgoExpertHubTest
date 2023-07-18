def blackjackProbability(target, startingHand):
    # Write your code here.
    memo = {}
    return round(recursion(target, startingHand, memo), 3)


def recursion(target, currentHand, memo):
    if currentHand in memo:
        return memo[currentHand]
        
    drawLimit = target - 4
    if currentHand > target:
        return 1
        
    if currentHand >= drawLimit:
        return 0






    totalProb = 0
    for limit in range(1, 11):
        totalProb += 0.1 * recursion(target, currentHand + limit, memo)
    memo[currentHand] = totalProb
    return totalProb