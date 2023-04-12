# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent




def findSuccessor(tree, node):
    # Write your code here.
    arr = inOrderTraversal(tree)
    for i in range(len(arr)):
        if i < len(arr) - 1:
            if arr[i] == node:
                return arr[i + 1]
        else:
            return None


def inOrderTraversal(tree, arr = []):
    if tree is None:
        return arr


    inOrderTraversal(tree.left, arr)
    arr.append(tree)
    inOrderTraversal(tree.right, arr)
    return arr