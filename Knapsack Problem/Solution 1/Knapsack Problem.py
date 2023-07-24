def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    array = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]
    for i in range(1, len(array)):
        value = items[i - 1][0]
        weight = items[i - 1][1]
        for j in range(len(array[0])):
            if weight <= j:
                array[i][j] = max(array[i-1][j], array[i-1][j-weight] + value)
            else:
                array[i][j] = array[i-1][j]
    return [array[-1][-1], getKnapsackItems(array, items)]


def getKnapsackItems(knapsack, items):
    sequence = []
    i = len(knapsack) - 1
    c = len(knapsack[0]) - 1
    while i > 0:
        if knapsack[i][c] == knapsack[i-1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))