def diceThrows(numDice, numSides, target):
    # Write your code here.
    storedResults = [[-1] * (target + 1) for _ in range(numDice + 1)]
    return diceThrowsHelper(numDice, numSides, target, storedResults)




def diceThrowsHelper(numDice, numSides, target, storedResults):
    if numDice == 0:
        return 1 if target == 0 else 0


    if storedResults[numDice][target] > -1:
        return storedResults[numDice][target]


    numWays = 0
    for currTarget in range(max(0, target - numSides), target):
        numWays += diceThrowsHelper(numDice - 1, numSides, currTarget, storedResults)
    storedResults[numDice][target] = numWays


    return numWays

