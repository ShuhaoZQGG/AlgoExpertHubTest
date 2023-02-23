def insertionSort(array):
    # Write your code here.
    counter = 0
    for i in range(1, len(array)):
        for j in range(counter, -1, -1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i -= 1
            else:
                break
        counter += 1
    return array

