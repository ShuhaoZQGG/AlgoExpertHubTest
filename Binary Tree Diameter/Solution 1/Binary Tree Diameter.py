# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def binaryTreeDiameter(tree):
    longestDiamter = 0
    # Write your code here.
    def recursive(tree):
        nonlocal longestDiamter
        if tree is None:
            return 0
        leftLongest = recursive(tree.left)
        rightLongest = recursive(tree.right)
        longestDiamter = max(longestDiamter, leftLongest + rightLongest)
        return 1 + max(leftLongest, rightLongest)
    recursive(tree)
    return longestDiamter