def getPermutations(array):
    # Write your code here.
    output = []
    recursion(array, [], output)
    return output
    
def recursion(array, permutation, permutations):
    if not(len(array)) and len(permutation):
        permutations.append(permutation)
    else:
        for i in range(len(array)):
            newPermutation = [array[i]] + permutation
            newArray = array[:i] + array[i+1:]
            recursion(newArray, newPermutation, permutations)