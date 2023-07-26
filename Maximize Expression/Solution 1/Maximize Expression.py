def maximizeExpression(array):
    # Write your code here.
    maximum = -float('inf')
    for a in range(len(array) - 3):
        localMax = 0
        localMax = array[a]
        aMax = localMax
        for b in range(a+1, len(array) - 2):
            localMax = aMax
            localMax -= array[b]
            bMax = localMax
            for c in range(b+1, len(array) - 1):
                localMax = bMax
                localMax += array[c]
                cMax = localMax
                for d in range(c+1, len(array)):
                    localMax = cMax
                    localMax -= array[d]
                    maximum = max(maximum, localMax)
    if maximum == -float('inf'):
        return 0
    return maximum


    