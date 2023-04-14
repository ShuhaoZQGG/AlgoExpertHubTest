# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if not tree1 and not tree2:
        return None
    if tree1 and tree2:
        tree1.value += tree2.value
    
    if not tree1.left and tree2.left:
        tree1.left = tree2.left
    elif tree1.left and tree2.left:
        mergeBinaryTrees(tree1.left, tree2.left)
    
    if not tree1.right and tree2.right:
        tree1.right = tree2.right
    elif tree1.right and tree2.right:
        mergeBinaryTrees(tree1.right, tree2.right)


    return tree1

