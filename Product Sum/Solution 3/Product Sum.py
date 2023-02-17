# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    
    def recursiveProductSum(array, factor):
        sum = 0
        for i in range(len(array)):
            if type(array[i]) is list:
                sum += recursiveProductSum(array[i], (factor + 1))
            else:
                sum += array[i]
        return sum * factor
    return recursiveProductSum(array, 1)



