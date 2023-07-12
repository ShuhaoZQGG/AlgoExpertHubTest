def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row, col = len(matrix) - 1, len(matrix[0]) - 1
    i, j = 0, col
    while i <= row and j >= 0:
        if matrix[i][j] == target:
            return [i,j]
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    return [-1, -1]

