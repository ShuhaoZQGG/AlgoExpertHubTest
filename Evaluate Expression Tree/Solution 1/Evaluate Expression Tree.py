# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def evaluateExpressionTree(tree):
    # Write your code here.
    return postOrderTraversal(tree)


def postOrderTraversal(tree):
    if tree.value >= 0:
        return tree.value
    leftVal = postOrderTraversal(tree.left)
    rightVal = postOrderTraversal(tree.right)
    if tree.value == -1:
        return leftVal + rightVal
    elif tree.value == -2:
        return leftVal - rightVal
    elif tree.value == -3:
        return int(leftVal / rightVal)
    else:
        return leftVal * rightVal