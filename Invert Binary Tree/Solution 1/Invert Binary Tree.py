def invertBinaryTree(tree):
    # Write your code here.
    if tree.left:
        invertBinaryTree(tree.left)
    if tree.right:
        invertBinaryTree(tree.right)
    if tree.left or tree.right:
        tree.right, tree.left = tree.left, tree.right
    else:
        return tree




# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

