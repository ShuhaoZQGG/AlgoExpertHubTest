import math
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, isBalanced):
        self.height = height
        self.isBalanced = isBalanced
def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(node):
    if node == None:
        return TreeInfo(-1, True)


    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)


    isBalanced = leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1
    return TreeInfo(height, isBalanced)