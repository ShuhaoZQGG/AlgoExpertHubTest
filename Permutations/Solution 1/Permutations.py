def getPermutations(array):
    # Write your code here.
    output = []
    recursion(array, [], output)
    return output


def recursion(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            recursion(newArray, newPermutation, permutations)
 