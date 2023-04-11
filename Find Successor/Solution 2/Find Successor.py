# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent




def findSuccessor(tree, node):
    # Write your code here.
    if node.right:
        return getLeftMostChild(node)
    return getRightMostParent(node)


def getLeftMostChild(node):
    currentNode = node.right
    while currentNode.left:
        currentNode = currentNode.left
    return currentNode


def getRightMostParent(node):
    while node.parent and node.parent.right == node:
        node = node.parent
    return node.parent
    