# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    treeInfo = TreeInfo(0, 0)
    if tree is None:
        treeInfo.diameter = 0
        treeInfo.height = 0
        return treeInfo
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)


    currentHeight = leftTreeInfo.height + rightTreeInfo.height
    currentDiameter = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    maxDiameter = max(currentHeight, currentDiameter)
    maxHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
    return TreeInfo(maxDiameter, maxHeight)
    

