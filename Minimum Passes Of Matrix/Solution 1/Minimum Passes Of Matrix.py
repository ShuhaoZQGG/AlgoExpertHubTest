def minimumPassesOfMatrix(matrix):
    # Write your code here.
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    queue = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] > 0:
                queue.append((i, j))


    ans = 0
    
    while queue:
        ans += 1
        length = len(queue)
        for i in range(length):
            r, c = queue.pop(0)
            for dr, dc in dirs:
                ROW, COL = r + dr, c + dc
                if ROW >= 0 and ROW < row and COL >= 0 and COL < col and matrix[ROW][COL] < 0:
                    matrix[ROW][COL] *= -1
                    queue.append((ROW, COL))
                    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] < 0:
                return -1
    return ans - 1
    
                