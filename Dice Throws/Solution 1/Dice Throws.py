def diceThrows(numDice, numSides, target):
    # Write your code here.
    storedResults = [[0] * (target + 1) for _ in range(numDice + 1)]
    storedResults[0][0] = 1


    for currNumDice in range(1, numDice + 1):
        for currTarget in range(target + 1):
            numWays = 0
            for currNumSides in range(1, min(currTarget, numSides) + 1):
                numWays += storedResults[currNumDice - 1][currTarget - currNumSides]
            storedResults[currNumDice][currTarget] = numWays
    return storedResults[numDice][target]

