import math
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    treeInfo = TreeInfo(0)
    return reconstructBstByRange(-float('inf'), float('inf'), preOrderTraversalValues, treeInfo)


def reconstructBstByRange(lowerBound, upperBound, preOrderTraversalValues, currentSubTreeInfo):
    idx = currentSubTreeInfo.rootIdx
    if len(preOrderTraversalValues) == idx:
        return None


    if preOrderTraversalValues[idx] < lowerBound or preOrderTraversalValues[idx] >= upperBound:
        return None
    currentSubTreeInfo.rootIdx += 1
    leftSubTree = reconstructBstByRange(lowerBound, preOrderTraversalValues[idx], preOrderTraversalValues, currentSubTreeInfo)
    rightSubTree = reconstructBstByRange(preOrderTraversalValues[idx], upperBound, preOrderTraversalValues, currentSubTreeInfo)
    return BST(preOrderTraversalValues[idx], leftSubTree, rightSubTree)

