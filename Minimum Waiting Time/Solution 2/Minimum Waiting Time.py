def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    sum = 0
    for i in range(len(queries)):
        sum += queries[i] * (len(queries) - i - 1)
    return sum