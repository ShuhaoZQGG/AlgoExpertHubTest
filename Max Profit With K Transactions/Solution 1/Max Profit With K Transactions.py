def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if len(prices) == 0:
        return 0
    matrix = [[[0,0] for i in prices] for j in range(k + 1)]
    for i in range(1, len(matrix)):
        localMaxProfit = float("-inf")
        for j in range(1, len(matrix[0])):
            localMaxProfit = max(localMaxProfit, matrix[i-1][j-1][1] - prices[j-1])
            matrix[i][j][0] = localMaxProfit
            matrix[i][j][1] = max(matrix[i][j-1][1], localMaxProfit + prices[j])
    print(matrix)
    return matrix[-1][-1][1]
            

