def numbersInPi(pi, numbers):
    # Write your code here.
    hashmap = { number: True for number in numbers }
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, hashmap, cache, i)
    return -1 if cache[0] == float("inf") else cache[0]


def getMinSpaces(pi, hashmap, cache, idx):
    if idx == len(pi):
        return -1


    if idx in cache:
        return cache[idx]


    minSpaces = float("inf")
    
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]
        if prefix in hashmap:
            minSpacesInSuffix = getMinSpaces(pi, hashmap, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]