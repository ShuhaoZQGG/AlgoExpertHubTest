def powerset(array):
    # Write your code here.
    output = []
    recursion(array, output)
    return output


def recursion(array, powersets):
    if array not in powersets:
        powersets.append(array)
    for i in range(len(array)):
        newArray = array[:i] + array[i+1:]
        recursion(newArray, powersets)