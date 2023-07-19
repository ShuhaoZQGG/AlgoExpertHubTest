def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    return recursion(0, 0, width, height)
    
    
def recursion(width, height, maxWidth, maxHeight):
    row, col = maxHeight - 1, maxWidth - 1
    if height == row and width == col:
        return 1
    else:
        if height + 1 <= row and width + 1 <= col:
            return recursion(width + 1, height, maxWidth, maxHeight) + recursion(width, height + 1, maxWidth, maxHeight)
        elif height + 1 <= row:
            return recursion(width, height + 1, maxWidth, maxHeight)
        else:
            return recursion(width + 1, height, maxWidth, maxHeight)


    