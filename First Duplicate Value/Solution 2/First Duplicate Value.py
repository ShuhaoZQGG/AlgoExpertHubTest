def firstDuplicateValue(array):
    # Write your code here.
    dict = {}
    for i in range(len(array)):
        if array[i] not in dict:
            dict[array[i]] = True
        else:
            return array[i]
    return -1

