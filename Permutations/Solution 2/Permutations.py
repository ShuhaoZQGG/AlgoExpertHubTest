def getPermutations(array):
    # Write your code here.
    output = []
    recursion(0, array, output)
    return output


def recursion(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            recursion(i + 1, array, permutations)
            array[i], array[j] = array[j], array[i]



