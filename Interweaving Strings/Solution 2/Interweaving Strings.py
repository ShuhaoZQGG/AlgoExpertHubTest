def interweavingStrings(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
        return False
    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]    
    return recursion(one, two, three, 0, 0, cache)


def recursion(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]
    k = i + j
    if k == len(three):
        return True
    if i < len(one) and one[i] == three[k]:
        cache[i][j] = recursion(one, two, three, i+1, j, cache)
        if cache[i][j]:
            return True
            
    if j < len(two) and two[j] == three[k]:
        cache[i][j] = recursion(one, two, three, i, j+1, cache)
        return cache[i][j]
    cache[i][j] = False
    return False