from collections import deque
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def symmetricalTree(tree):
    # Write your code here.
    if tree is None:
        return True
    if (tree.left and not(tree.right)) or (tree.right and not(tree.left)):
        return False
    leftSubTree = tree.left
    rightSubTree = tree.right


    leftSubStack, rightSubStack = deque([leftSubTree]), deque([rightSubTree])
    
    while leftSubStack and rightSubStack:
        leftNode = leftSubStack.popleft()
        rightNode = rightSubStack.popleft()
        if leftNode and rightNode:
            if leftNode.value != rightNode.value:
                return False
            if leftNode.left:
                leftSubStack.append(leftNode.left)
            if leftNode.right:
                leftSubStack.append(leftNode.right)
            if rightNode.right:
                rightSubStack.append(rightNode.right)
            if rightNode.left:
                rightSubStack.append(rightNode.left)
    if (leftSubStack and not rightSubStack) or (not leftSubStack and rightSubStack):
        return False
    return True     


# def isSymmetrical(array):
#     i, j = 0, len(array) - 1
#     while i <= j:
#         if array[i] == array[j]:
#             continue
#         else:
#             return False
#     return True
        