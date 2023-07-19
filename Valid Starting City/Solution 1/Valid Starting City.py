def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    return recursion(distances, fuel, mpg, 0, 0)
def recursion(distances, fuel, mpg, index, allowableDistance):
    for i in range(index, len(distances)):
        allowableDistance += fuel[i] * mpg
        if allowableDistance < distances[i]:
            return recursion(distances, fuel, mpg, index + 1, 0)
        else:
            allowableDistance -= distances[i]
            continue
    for i in range(0, index):
        allowableDistance += fuel[i] * mpg
        if allowableDistance < distances[i]:
            return recursion(distances, fuel, mpg, index + 1, 0)
        else:
            allowableDistance -= distances[i]
            continue
    return index