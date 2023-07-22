def minNumberOfJumps(array):
    # Write your code here.
    index = len(array) - 1
    counter = 0
    while index > 0:
        for i in range(index, -1, -1):
            if index - i <= array[i]:
                localIndex = i
        counter += 1
        index = localIndex
    return counter