def transposeMatrix(matrix):
    # Write your code here.
    row = len(matrix)
    col = len(matrix[0])


    transpose = [[0] * row for _ in range(col)]


    for i in range(row):
        for j in range(col):
            transpose[j][i] = matrix[i][j]


    return transpose