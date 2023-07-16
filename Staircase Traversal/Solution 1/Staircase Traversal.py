def staircaseTraversal(height, maxSteps):
    # Write your code here.
    if height == 0:
        return 1
    res = 0 
    for i in range(1, maxSteps + 1):
        if i <= height:
            res += staircaseTraversal(height - i, maxSteps)
    return res
        