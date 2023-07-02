from collections import deque
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def rightSiblingTree(root):
    # Write your code here.
    q = [(root, 0)]
    while q:
        node, lvl = q.pop(0)
        if node is None:
            continue
        q.append((node.left, lvl + 1))
        q.append((node.right, lvl + 1))
        nextNode = q[0]
        if lvl == nextNode[1]:
            node.right = nextNode[0]
        else:
            node.right = None
    return root