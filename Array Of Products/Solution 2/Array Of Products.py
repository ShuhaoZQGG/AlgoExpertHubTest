import math
def arrayOfProducts(array):
    # Write your code here.
    sums = []
    for index, _ in enumerate(array):
        sums.append(1 * math.prod(array[:index]) * math.prod(array[index+1:]))
    return sums

