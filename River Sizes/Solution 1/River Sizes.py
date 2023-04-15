def riverSizes(matrix):
    # Write your code here.
    ans = []
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    stack = []
    size = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            stack.append((i, j))
            while stack:
                node = stack.pop()
                row, col = node
                if matrix[row][col] == 1 and (row, col) not in visited:
                    size += 1
                    for dir in dirs:
                        dr, dc = dir
                        ROW, COL = row + dr, col + dc
                        if ROW >= 0 and ROW < len(matrix) and COL >= 0 and COL < len(matrix[0]):
                            stack.append((ROW, COL))
                visited.add((row, col))
            if size > 0:
                ans.append(size)
            size = 0
    return ans


            

