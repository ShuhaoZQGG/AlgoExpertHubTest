def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    leastAllowableDistance = 0
    city = 0
    currentAllowableDistance = 0
    for i in range(len(distances)):
        if currentAllowableDistance < leastAllowableDistance:
            leastAllowableDistance = currentAllowableDistance
            city = i
        currentAllowableDistance += fuel[i] * mpg - distances[i]
    return city

