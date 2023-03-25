def levenshteinDistance(str1, str2):
    # Write your code here.
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    matrix = [[0] * (len(big) + 1) for _ in range(len(small) + 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                matrix[i][j] = 0
            elif i == 0:
                matrix[i][j] = matrix[i][j-1] + 1
            elif j == 0:
                matrix[i][j] = matrix[i-1][j] + 1
            elif small[i-1] == big[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
    return matrix[-1][-1]

