def selectionSort(array):
    # Write your code here.
    i = 0
    while i < len(array) - 1:
         j, smallest = i, i
         while j < len(array) - 1:
             j += 1
             if array[j] < array[smallest]:
                 smallest = j
         array[i], array[smallest] = array[smallest], array[i]
         i += 1
    return array