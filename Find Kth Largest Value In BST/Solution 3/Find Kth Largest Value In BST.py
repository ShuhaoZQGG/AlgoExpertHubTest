# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def findKthLargestValueInBst(tree, k):
    # Write your code here.
    arr = postOrderTraversal(tree, [])
    return arr[k-1]


def postOrderTraversal(tree, arr):
    if tree.right:
        postOrderTraversal(tree.right, arr)
    arr.append(tree.value)
    if tree.left:
        postOrderTraversal(tree.left, arr)
    return arr

