# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def symmetricalTree(tree):
    # Write your code here.
    if not tree:
        return True


    q = [(tree.left, tree.right)]
    while q:
        left, right = q.pop(0)
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.value != right.value:
            return False
        q.append((left.left, right.right))
        q.append((left.right, right.left))
    return True

