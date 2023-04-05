# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    global level
    level = 0
    return reconstructBstByRange(-float('inf'), float('inf'), preOrderTraversalValues)


def reconstructBstByRange(lowerBound, upperBound, preOrderTraversalValues):
    global level
    if len(preOrderTraversalValues) == level:
        return None
    rootValue = preOrderTraversalValues[level]


    if rootValue < lowerBound or rootValue >= upperBound:
        return None
    level += 1
    leftSubTree = reconstructBstByRange(lowerBound, rootValue, preOrderTraversalValues)
    rightSubTree = reconstructBstByRange(rootValue, upperBound, preOrderTraversalValues)
    return BST(rootValue, leftSubTree, rightSubTree)