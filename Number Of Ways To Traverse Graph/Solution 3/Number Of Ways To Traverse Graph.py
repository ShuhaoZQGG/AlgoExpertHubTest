def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    cache = [[1 for j in range(width)] for i in range(height)]
    row, col = height -1, width - 1
    for i in range(row, -1, -1):
        for j in range(col, -1, -1):
            if i + 1 <= row and j + 1 <= col:
                cache[i][j] = cache[i][j+1] + cache[i+1][j]
            elif i + 1 <= row:
                cache[i][j] = cache[i+1][j]
            elif j + 1 <= col:
                cache[i][j] = cache[i][j+1]
    return cache[0][0]