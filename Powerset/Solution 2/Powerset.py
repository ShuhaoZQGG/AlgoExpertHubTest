def powerset(array):
    # Write your code here.
    output = [[]]
    for el in array:
        for i in range(len(output)):
            output.append(output[i] + [el])
    return output
        

