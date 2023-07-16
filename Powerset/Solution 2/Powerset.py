def powerset(array):
    # Write your code here.
    output = [[]]
    for i in range(len(array)):
        for j in range(len(output)):
            output.append([array[i]] + output[j])
    return output
        

