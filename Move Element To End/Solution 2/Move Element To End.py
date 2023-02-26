def moveElementToEnd(array, toMove):
    # Write your code here.
    for i in range(len(array)):
        el = array[i]
        if el != toMove:
            array.pop(i)
            array.insert(0, el)
    return array
        

