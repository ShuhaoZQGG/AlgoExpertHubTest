# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def flattenBinaryTree(root):
    # Write your code here.
    q = [root]
    visited = set()
    head = ptr = BinaryTree(None)
    while q:
        node = q[-1]
        if node.left and node.left not in visited:
            q.append(node.left)
            visited.add(node.left)
        else:
            nodeToRemove = q.pop()
            if nodeToRemove.right:
                q.append(nodeToRemove.right)
            nodeToRemove.left = ptr
            ptr.right = nodeToRemove
            ptr = ptr.right
    newHead = head.right
    head.right.left = None
    head.right = None
    return newHead
            

