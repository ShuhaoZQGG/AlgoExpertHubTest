def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    cache = [[0 for j in range(width)] for i in range(height)]
    recursion(0, 0, cache)
    return cache[0][0]
    
def recursion(width, height,cache):
    row, col = len(cache) - 1, len(cache[0]) - 1
    if height == row and width == col:
        cache[height][width] = 1
        return 1
    else:
        if height + 1 <= row and width + 1 <= col:
            recursion(width + 1, height, cache)
            recursion(width, height + 1, cache)
            cache[height][width] = cache[height][width + 1] + cache[height + 1][width]
        elif height + 1 <= row:
            recursion(width, height + 1, cache)
            cache[height][width] = cache[height + 1][width]
        else:
            recursion(width + 1, height, cache)
            cache[height][width] =  cache[height][width + 1]
    