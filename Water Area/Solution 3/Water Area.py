def waterArea(heights):
    # Write your code here.
    i = 0
    prevHeight = 0
    total = 0
    while i < len(heights):
        if prevHeight == 0 and heights[i] == 0:
            i += 1
        else:
            nextWall = GetNextWall(heights, i)
            prevHeight = heights[i]
            if nextWall is None:
                break
            nextHeight = min(heights[nextWall], prevHeight)


            for j in range(i + 1, nextWall):
                total += nextHeight - heights[j]
            i = nextWall
    return total


def GetNextWall(heights, start):
    currHeight = heights[start]
    maxHeight = 0
    for i in range(start + 1, len(heights)):
        if heights[i] >= currHeight:
            return i
        if heights[i] > maxHeight:
            maxHeight, maxIndex = heights[i], i
    if maxHeight > 0:
        return maxIndex
    else:
        return None