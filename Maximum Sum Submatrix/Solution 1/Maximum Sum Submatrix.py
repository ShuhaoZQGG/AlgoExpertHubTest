def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    maximumValue = -float('inf')
    rowIdx, colIdx = 0, 0
    output = getSizesOfSubmatrix(matrix, size, rowIdx, colIdx, maximumValue)
    return output


def getSizesOfSubmatrix(matrix, size, rowIdx, colIdx, maximumValue):
    row, col = rowIdx + size, colIdx + size
    res = 0
    for i in range(rowIdx,row):
        for j in range(colIdx,col):
           print(i, j)
           res += matrix[i][j]
    maximumValue = max(maximumValue, res)
    if row == len(matrix) and col == len(matrix[0]):
        return maximumValue
    if col < len(matrix[0]):
        maximumValue = getSizesOfSubmatrix(matrix, size, rowIdx, colIdx + 1, maximumValue)
    if col == len(matrix[0]):
        maximumValue = getSizesOfSubmatrix(matrix, size, rowIdx + 1, 0, maximumValue)
    return maximumValue