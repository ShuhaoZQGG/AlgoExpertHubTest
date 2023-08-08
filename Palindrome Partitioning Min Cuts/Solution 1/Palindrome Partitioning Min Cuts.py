def palindromePartitioningMinCuts(string):
    # Write your code here.
    matrix = [[0 for i in range(0, len(string))] for j in range(0, len(string))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = isPalindrome(string[i:j+1])
    cuts = [float("inf") for i in string]
    for i in range(len(string)):
        if matrix[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1
            for j in range(1, i):
                if matrix[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j-1] + 1
    print(matrix)
    print(cuts)
    return cuts[-1]


def isPalindrome(string):
    return string == string[::-1]