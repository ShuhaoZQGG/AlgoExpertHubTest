from itertools import chain


def removeIslands(matrix):
    # Write your code here.
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = set()
    top, bottom = 0, len(matrix[0]) - 1
    left, right = 0, len(matrix) - 1
    print(top, bottom)
    print(left, right)
    ans = []
    q = []
    for i in range(right + 1):
        for j  in range(bottom + 1):
            if matrix[i][j] == 1:
                q.append((i, j))            
            subAns = []
            while q:
                row, col = q.pop()
                if matrix[row][col] == 1 and (row, col) not in visited:
                    subAns.append((row, col))
                    for dir in dirs:
                        dr,dc = dir
                        ROW, COL = row + dr, col + dc
                        if ROW >= left and ROW <= right and COL >= top and COL <= bottom:
                            q.append((ROW, COL))
                visited.add((row, col))
            if subAns != []:
                ans.append(subAns)
 
    i = 0
    while i < len(ans):
        el = ans[i]
        print(el)
        for subEl in el:
            row, col = subEl
            if row == left or row == right or col == top or col == bottom:
                del ans[i]
                i -= 1
                break
        i += 1
                
    ans = list(chain.from_iterable(ans))
    for el in ans:
        r, c = el
        matrix[r][c] = 0
    return matrix