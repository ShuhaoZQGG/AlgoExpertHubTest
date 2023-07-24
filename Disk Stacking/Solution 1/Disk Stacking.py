import math
def diskStacking(disks):
    # Write your code here.
    maxHeight = -math.inf
    ans = []
    disks.sort()
    for i in range(len(disks)):
        disk = disks[i]
        otherDisks = disks[:i] + disks[i+1:]
        height, combination = findCombination(disk, otherDisks, 0, [])
        if height > maxHeight:
            maxHeight = height
            ans = combination
    return ans


def findCombination(disk, otherDisks, currHeight, combination):
    combination.append(disk)
    width, depth, height = disk
    currHeight += height
    for i in range(len(otherDisks)):
        DISK = otherDisks[i]
        autreDisks = otherDisks[:i] + otherDisks[i+1:]
        w, d, h = DISK
        if w > width and d > depth and h > height:
            return findCombination(DISK, autreDisks, currHeight, combination)
    return (currHeight, combination)