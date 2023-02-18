def isMonotonic(array):
    # Write your code here.
    nonIncreasing = False
    nonDecreasing = False
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            nonIncreasing = True
        elif array[i] > array[i + 1]:
            nonDecreasing = True
            
    if nonIncreasing == True and nonDecreasing == True:
        return False


    else:
        return True

