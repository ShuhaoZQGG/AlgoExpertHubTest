# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def splitBinaryTree(tree):
    # Write your code here.
    sum = getSum(tree)
    if ifSubTreeSumEqualsTarget(tree, sum / 2):
        return sum / 2
    else:
        return 0


def ifSubTreeSumEqualsTarget(tree, target):
    if tree is None:
        return False
    if getSum(tree) == target:
        return True
    if ifSubTreeSumEqualsTarget(tree.left, target):
        return True
    if ifSubTreeSumEqualsTarget(tree.right, target):
        return True
    return False


def getSum(tree):
    if tree is None:
        return 0
    leftTree = getSum(tree.left)
    rightTree = getSum(tree.right)
    return leftTree + rightTree + tree.value
        

