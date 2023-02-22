def arrayOfProducts(array):
    # Write your code here.
    i = 0
    ans = []
    while i < len(array):
        product = 1
        for j in range(len(array)):
            if i != j:
                product *= array[j]
        ans.append(product)
        i += 1
    return ans

